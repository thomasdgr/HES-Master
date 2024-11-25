import os
import json
import tqdm
import requests
import pandas as pd
from bs4 import BeautifulSoup

from chromadb import PersistentClient
from chromadb.utils import embedding_functions

from langchain.llms.ollama import Ollama
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PDFMinerLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain.chains import ConversationalRetrievalChain, RetrievalQA


class RAG():
    def __init__(
        self,
        model_type: str,
        vector_type: str,
        input_path: str,
        db_path: str,
        api_endpoint: str,
        api_key: str = None,
    ):

        self.model_type = model_type
        self.vector_type = vector_type
        self.db_path = db_path
        self.input_path = input_path
        self.api_endpoint = api_endpoint
        self.api_key = api_key

        self.model = GPTModel(
            key=self.api_key,
            model_name=self.model_type,
            api_endpoint=self.api_endpoint
        ) if "gpt" in model_type else OllamaModel(
            model_name=self.model_type,
            api_endpoint=self.api_endpoint
        )

        self.rag = FaissRAG(
            input_path=self.input_path,
            db_path=self.db_path,
            api_key=self.api_key
        ) if vector_type == "faiss" else ChromaRAG(
            input_path=self.input_path,
            db_path=self.db_path,
            api_key=self.api_key
        )

    def generate_chat_completion(
        self,
        user_prompt: str
    ):

        return self.model.generate_chat_completion(
            user_prompt,
            self.rag
        )


class GPTModel():
    def __init__(
        self,
        key: str,
        model_name: str,
        api_endpoint: str
    ):

        self.key = key
        self.api_endpoint = api_endpoint
        self.model = model_name

    def generate_chat_completion(
        self,
        user_prompt: str,
        rag: RAG
    ):

        passages = rag.find_passages(user_prompt)
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.key}",
        }

        def create_sys_prompt(
            passages: str
        ):
            return f"""Tu es un assistant qui répond aux questions en français
uniquement. Tu as à ta disposition des informations et des réglementations sur
la haute école d'ingénierie et d'architecture de Fribourg en Suisse. Si la
question porte sur un ou plusieurs passages textuels, utilisez-les pour
répondre à la question mais ne les paraphrase pas. Si la question ne porte sur
aucun passage textuel, générez une réponse à partir de tes connaissances.
Assure-toi de toujours fournir la réponse, la source de l'information et de
mentionner dans quel fichier l'information a été trouvée en utilisant le
format suivant:
Document: <document name>
<answer>

# Start of passages
{passages}
# End of passages
"""

        data = {
            "model": self.model,
            "messages": [
                {
                    "role": "system",
                    "content": create_sys_prompt(passages)
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
            "temperature": 0.2,
        }

        response = requests.post(
            self.api_endpoint,
            headers=headers,
            data=json.dumps(data)
        )

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        elif response.status_code == 500:
            return self.generate_chat_completion(user_prompt)
        else:
            raise Exception(f"Error {response.status_code}: {response.text}")


class OllamaModel():
    def __init__(
        self,
        model_name: str,
        api_endpoint: str
    ):

        self.api_endpoint = api_endpoint
        self.model = Ollama(
            model=model_name,
            base_url=self.api_endpoint,
            temperature=0.2,
            stop=["[/INST]", "</s>", "<|im_end|>", "<</SYS>>"],
        )

    def generate_chat_completion(
        self,
        user_prompt: str,
        rag: RAG
    ) -> str:

        def create_sys_prompt():
            return PromptTemplate(
                input_variables=["context", "question"],
                template="""<s>[INST]<<SYS>>Tu es un assistant qui répond aux
questions en français. Tu as à ta disposition des informations sur la haute
école d'ingénierie et d'architecture de Fribourg en Suisse. Si la question
portesur un ou plusieurs passages textuels, utilisez-les pour répondre à la
question mais ne les paraphrase pas. Si la question ne porte sur aucun passage
textuel, générez une réponse à partir de tes connaissances.
{context}<</SYS>>{question}[/INST]""",
            )

        chain: ConversationalRetrievalChain = RetrievalQA.from_chain_type(
            self.model,
            retriever=rag.db_client.as_retriever(search_kwargs={"k": 4}),
            chain_type_kwargs={"prompt": create_sys_prompt()},
            input_key="question",
            output_key="answer",
            return_source_documents=True,
        )

        res = chain(
            {
                "question": user_prompt,
            }
        )

        def prepare_document(x):
            return x if x is None else os.path.basename(x)

        def prepare_page(x):
            return x if x is None else int(x) + 1

        def prepare_source(x):
            return {
                "document": prepare_document(x.metadata.get("source", None)),
                "page": prepare_page(x.metadata.get("page", None)),
                "chunk": x.page_content,
            }

        response = ""
        for s in res.get("source_documents"):
            source = prepare_source(s)
            response += f"Document: {source['document']}\n"
            # if source['page']:
            #     response += f"Page {source['page']}: "
            # response += f"{source['chunk']}\n\n"
        return response + "\n" + res.get("answer")


class ChromaRAG:
    def __init__(
        self,
        input_path: str,
        db_path: str,
        api_key: str,
    ):

        # See https://docs.trychroma.com/embeddings for more information
        # self.ef = self.e5_embedding("cuda:0")  # - SBERT
        # self.ef = self.BAAI_embedding(api_key)  # - BGE-M3
        self.ef = self.gpt3_embedding(api_key)

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=20,
            length_function=len,
        )

        self.db_client = PersistentClient(path=db_path)
        self.collection = self.build_collection(input_path)

    def e5_embedding(
        self,
        device: str = "cpu"
    ):
        return embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="intfloat/multilingual-e5-large",
            device=device
            # device="cuda:0"
        )

    def gpt3_embedding(
        self,
        key: str,
    ):
        return embedding_functions.OpenAIEmbeddingFunction(
                api_key=key,
                model_name="text-embedding-3-large"
            )

    def BAAI_embedding(
        self,
        key: str,
    ):
        return embedding_functions.HuggingFaceEmbeddingFunction(
            api_key=key,
            model_name="BAAI/bge-m3"
        )

    def build_collection(
        self,
        input_path: str
    ):

        collection = self.db_client.get_or_create_collection(
            embedding_function=self.ef,
            name="collec",
            metadata={"hnsw:space": "cosine"}
        )
        if collection.count() == 0:
            for file in os.listdir(input_path):
                if file.endswith(".pdf"):
                    loader = PDFMinerLoader(f"{input_path}/{file}")
                    docs = loader.load_and_split(self.splitter)
                    for i, doc in enumerate(tqdm.tqdm(docs)):
                        collection.add(
                            ids=f"{file}-{i}",
                            documents="passage: " + doc.page_content,
                            metadatas={"source": file}
                        )
                elif file.endswith(".csv"):
                    df = pd.read_csv(f"{input_path}/{file}")
                    for i, row in df.iterrows():
                        passage = " ".join(row.astype(str))
                        collection.add(
                            ids=f"{file}-{i}",
                            documents="passage: " + passage,
                            metadatas={"source": file}
                        )
                elif file.endswith(".json"):
                    with open(f"{input_path}/{file}", 'r') as json_file:
                        websites = json.load(json_file)
                    for website in websites:
                        response = requests.get(website["address"])
                        if response.status_code == 200:
                            soup = BeautifulSoup(
                                response.text,
                                'html.parser'
                            )
                            passage = " ".join(
                                [
                                    p.get_text()
                                    for p in soup.find_all('p')
                                ]
                            )
                            if passage:
                                collection.add(
                                    ids=f"{website['name']}",
                                    documents="passage: " + passage,
                                    metadatas={"source": website["address"]}
                                )

        return collection

    def find_passages(
        self,
        query: str
    ):

        res = self.collection.query(
            query_texts=f"query: {query}",
            n_results=2
        )
        output = []
        for document, metadata in zip(
            res["documents"][0],
            res["metadatas"][0]
        ):
            output.append(f"## {metadata['source']}\n{document[9:]}")
        return "\n\n".join(output)


class FaissRAG:
    def __init__(
        self,
        input_path: str,
        db_path: str,
        api_key: str,
    ):

        # self.ef = self.BAAI_embedding("cuda:0")
        self.ef = self.gpt3_embedding(api_key)

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=20,
            length_function=len,
        )

        self.db_client = FAISS.load_local(
            db_path,
            self.ef,
            "faiss_index",
            allow_dangerous_deserialization=True
        )
        self.build_collection(
            input_path,
            db_path
        )

    def gpt3_embedding(
        self,
        key: str,
    ):
        return OpenAIEmbeddings(
            deployment="text-embedding-3-large",
            openai_api_key=key
        )

    def BAAI_embedding(
        self,
        device: str = "cpu"
    ):
        return HuggingFaceBgeEmbeddings(
            model_name="BAAI/bge-m3",
            model_kwargs={"device": device},
            encode_kwargs={"normalize_embeddings": True},
        )

    def build_collection(
        self,
        input_path: str,
        db_path: str
    ):
        first_doc = True
        if self.db_client is None:
            for file in os.listdir(input_path):
                if file.endswith(".pdf"):
                    loader = PDFMinerLoader(f"{input_path}/{file}")
                    docs = loader.load_and_split(self.splitter)
                elif file.endswith(".csv"):
                    df = pd.read_csv(f"{input_path}/{file}")
                    docs = [
                        " ".join(row.astype(str))
                        for _, row in df.iterrows()
                    ]
                elif file.endswith(".json"):
                    with open(f"{input_path}/{file}", 'r') as json_file:
                        websites = json.load(json_file)
                    for website in websites:
                        response = requests.get(website["address"])
                        if response.status_code == 200:
                            soup = BeautifulSoup(
                                response.text,
                                'html.parser'
                            )
                            docs = [
                                " ".join(
                                    [
                                        p.get_text()
                                        for p in soup.find_all('p')
                                    ]
                                )
                            ]
                            if docs:
                                if first_doc:
                                    self.db_client = FAISS.from_documents(
                                        documents=docs,
                                        embedding=self.ef,
                                    )
                                    first_doc = False
                                else:
                                    self.db_client.merge_from(
                                        FAISS.from_documents(
                                            documents=docs,
                                            embedding=self.ef,
                                        )
                                    )
                    continue
                if first_doc:
                    self.db_client = FAISS.from_documents(
                        documents=docs,
                        embedding=self.ef,
                    )
                    first_doc = False
                else:
                    self.db_client.merge_from(
                        FAISS.from_documents(
                            documents=docs,
                            embedding=self.ef,
                        )
                    )
            self.db_client.save_local(
                folder_path=db_path,
                index_name="faiss_index",
            )

    def find_passages(
        self,
        query: str
    ):

        searchDocs = self.db_client.similarity_search(query)
        return searchDocs[0].page_content

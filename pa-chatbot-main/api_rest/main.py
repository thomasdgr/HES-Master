import os
import logging

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.openapi.utils import get_openapi

from pydantic import BaseModel

from starlette.responses import FileResponse
from starlette.middleware.cors import CORSMiddleware

from api_rest.model.rag import RAG


# *****************************************************************************
#                  Some general constants and variables
# *****************************************************************************
NAME = 'Chatbot API'
VERSION = '1.0.0'
DESCRIPTION = 'Microservice to expose RAG model through a custom HEIA chatbot.'
BASE_URL: str = "http://chatbot.kube.isc.heia-fr.ch/"
URL_PREFIX: str = os.getenv("URL_PREFIX") or ""
SERVER_ADDRESS: str = os.getenv("SERVER_ADDRESS") or ""

# *****************************************************************************
#                  FastAPI entry point declaration
# *****************************************************************************
rootapp = FastAPI()

app = FastAPI(openapi_url='/specification')
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=NAME,
        version=VERSION,
        description=DESCRIPTION,
        routes=app.routes,
    )
    if SERVER_ADDRESS != "":
        openapi_schema["servers"] = [
            {
                "url": BASE_URL + URL_PREFIX,
                "description": "PA chatbot project."
            }
        ]
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
rootapp.mount(URL_PREFIX, app)
logger = logging.getLogger("uvicorn.error")
logger.info('Starting app with URL_PREFIX=' + URL_PREFIX)

# *****************************************************************************
#                  The classes defining the API input and output models
# *****************************************************************************


class Chat(BaseModel):
    query: str

# *****************************************************************************
#                  Routes of the API
# *****************************************************************************


@rootapp.on_event("startup")
def startup_event():
    global model

    # Version with faiss embeddings and phi3 model
    model = RAG(
        model_type="phi3",
        vector_type="faiss",
        input_path="./api_rest/documents",
        db_path="./api_rest/db/db_faiss_gpt3",
        api_endpoint="https://ollama.kube.isc.heia-fr.ch",
        api_key=os.getenv("OPENAI_API_KEY")
    )

    # Version with chroma embeddings and gpt-4o model
    # model = RAG(
    #     model_type="gpt-4o",
    #     vector_type="chroma",
    #     input_path="./api_rest/documents",
    #     db_path="./api_rest/db/db_chroma_gpt3",
    #     api_endpoint="https://api.openai.com/v1/chat/completions",
    #     api_key=os.getenv("OPENAI_API_KEY")
    # )

    embeddings = model.db_path.split('/')[-1].split('_')[1:]
    logger.info(f"""RAG model loaded using "{model.model_type}" \
model, "{embeddings[0]}" VectorDB and "{embeddings[1]}" embeddings."""
                )


@app.get("/")
def info():
    return JSONResponse(
        {
            'message': 'Welcome to our chatbot.'
                       'Try out /docs for the doc.'
                       'Try out /showcase for the showcase.'
                       'Try out /specification for the OpenAPI specification.'
        },
        status_code=200
    )


@app.get("/showcase")
def showcase():
    return FileResponse(
        "./api_rest/showcase/index.html"
        )


@app.get("/assets/{filename}")
async def assets(filename: str):
    return FileResponse(
        "./api_rest/showcase/assets/" + filename
        )


@app.post("/compute")
async def chat_completion(chat: Chat):
    return JSONResponse(
        {
            "response": model.generate_chat_completion(
                chat.query
            )
        },
        status_code=200
    )

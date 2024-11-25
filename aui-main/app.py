from flask import Flask, request, jsonify, send_from_directory
import ollama
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import os

nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__, static_folder='')

def analyze_importance(message):
    words = word_tokenize(message)
    words_alphanum = [word for word in words if word.isalnum()]
    
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words_alphanum if word.lower() not in stop_words]
    word_freq = Counter(filtered_words)
    most_common = word_freq.most_common(10)
    important_words = set(word for word, _ in most_common)

    highlighted_message = []
    for word in words:
        if word in important_words or not word.isalnum():
            highlighted_message.append(f'<span style=\"color: red;\">{word}</span>')
        else:
            highlighted_message.append(word)
    
    return ' '.join(highlighted_message)


conversation_context = []
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')

    conversation_context.append({'role': 'user', 'content': user_message})
    response = ollama.chat(model='mistral', messages=conversation_context)
    assistant_message = response['message']['content']
    conversation_context.append({'role': 'assistant', 'content': assistant_message})

    highlighted_input = analyze_importance(user_message)
    return jsonify({'message': assistant_message, 'prompt': highlighted_input})

@app.route('/')
def index():
    return send_from_directory('', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)

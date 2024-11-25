# Ragfish - Chatbot demo for HEIA-FR

## Setup

```sh
  python3 -m venv venv
  source ./venv/bin/activate
  pip install --upgrade pip
  pip install -r ./api_rest/requirements.txt
  export OPENAI_API_KEY="YOUR_API_KEY"
```

## Usage

```sh
  uvicorn api_rest.main:rootapp --reload
```

## Test

```sh
curl -H "Content-Type: application/json" \
     -H "accept: application/json" \
     -d '{
            "query": "Combien de crédits ECTS faut-il pour valider un Bachelor en informatique ?",
          }' \
     -X POST http://chatbot.kube.isc.heia-fr.ch/compute
```
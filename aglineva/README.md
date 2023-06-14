# Agileneva - 

This microservice, produced by **Agileneva** for **TSoft-Eng** course at HES-SO Master aims to provide users with a convenient and user-friendly way to search for and discover restaurants, as well as view ratings and reviews from other users. 

## Description of the project

Authors:
- Thomas Dagier
- Antoine Blancy
- Dorian Bernasconi
- Romain Peretti
- Thibault Michaud
- Simon Cirilli
- Kiady Arintsoa
- Anthony Chevrolet

Select, update, add notes or restaurants and sort a list of favorites in Lausanne. The project is dockerized and can be run with docker-compose. The frontend implements a Vue.js store to manage the state of the application. The backend is a REST API with a swagger interface using python FastAPI and Uvicorn. The database is a simple JSON file that is update depending on the endpoint called.

Units tests are implemented for the backend in order to test the endpoints and the database. A CI-CD pipeline is implemented with Github Actions. The pipeline is triggered on push on the main branch. It runs the unit tests for the backend and build the app if the tests pass.

It is also possible to push the docker image to the github container registry. In order to build and push, you must use the github actions secret `CR_PAT` with a personal access token with the `write:packages` scope. The docker image is then available in the github container registry depending the name given in the `docker-compose.yml` file.

## Running the web service - linux / mac

### Backend

The backend is in the folder `/backend/`. We used uvicorn and fastapi for the development. You may use an own
Python virtual environment in the `/backend/` folder installing the python modules from `/api_rest/requirements.txt`.

- Tools should work with python3.They were used with **python 3.7**, **python 3.8** and **python 3.9**.
- Clone the repository, create virtualenv, activate the virtual env, install required packages and test.

```sh
  cd backend/
  python3.8 -m venv venv
  source ./venv/bin/activate
  pip install --upgrade pip
  pip3 install --trusted-host pypi.python.org -r api_rest/requirements.txt
  uvicorn api_rest.main:rootapp --reload
```

Once installed, you may launch `uvicorn api_rest.main:rootapp --reload` to launch it from the terminal. The OpenAPI specifications are available under the route `/specification` and the Swagger interface to test the API under the route `/docs`. The showcase is under the route `/showcase`.

### Frontend

The frontend is in the folder `/frontend/`. We used vue.js and node for the development. When you are in the folder `/frontend/`, you may use the following commands to install the dependencies, type-check, build and run the showcase:

```sh
  cd frontend/api_rest/showcase/agilneva-fe
  npm install
  npm run type-check
  npm run build
  python3 -m http.server 5173
```

Once the frontend build, you may launch `python3 -m http.server 5173` to launch it from the terminal. The showcase is available under the route `http://localhost:5173/`.

## Running the service - docker

You may also use Docker (in root folder):

```sh
  docker-compose up -d 
```

When all the containers are up, you may access the frontend at `http://localhost:5173/` and the backend at `http://localhost:8000/`. 

To stop the service:

```sh
  docker-compose down -v
```

## Testing the service

If you want to test the app, you may use the following command:

```sh
  cd /backend/api_rest/
  pytest -s -p no:warnings
```

import os
import logging
import json

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from starlette.responses import FileResponse
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel, conint
from starlette.responses import JSONResponse

# *****************************************************************************
#                  Some general constants and variables
# *****************************************************************************
NAME = 'Agileneva API'
VERSION = '1.0.0'
DESCRIPTION = 'Agileneva MS for Software Engineering course at HES-SO Master.'
URL_PREFIX: str = os.getenv("URL_PREFIX") or ""
SERVER_ADDRESS: str = os.getenv("SERVER_ADDRESS") or ""
EXPOSED_ADDRESS: str = "https://myserver.com/"

# *****************************************************************************
#                  FastAPI entry point declaration
# *****************************************************************************
rootapp = FastAPI()

app = FastAPI(openapi_url='/specification')
app.add_middleware(CORSMiddleware, allow_origins=["*"], 
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(title=NAME, version=VERSION, 
        description=DESCRIPTION, routes=app.routes,)
    openapi_schema["info"]["x-logo"] = {"url": "assets/logo.png"}
    if SERVER_ADDRESS != "":
        openapi_schema["servers"] = [
            {"url": EXPOSED_ADDRESS + URL_PREFIX, 
            "description": "Agileneva API server"},
        ]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
rootapp.mount(URL_PREFIX, app)
logger = logging.getLogger("uvicorn.error")
logger.info('Starting app with URL_PREFIX=' + URL_PREFIX)

RESTOS_FILE = "restaurants.json"
restos = {}
with open(RESTOS_FILE, "r") as f:
    restos = json.load(f)

# *****************************************************************************
#                  The classes defining the API input and output models
# *****************************************************************************

class grade(BaseModel):
    resto: str
    name: str
    grade: conint(ge=1, le=5)

# *****************************************************************************
#                  Routes of the API
# *****************************************************************************

@app.on_event("startup")
def startup_event():
    pass
    
@app.get("/")
def info():
    return {'message': 'Welcome to the Agileneva API.'
                       'Try out /showcase for the demo or /docs for the doc.'}

@app.get("/showcase")
def showcase():
    logger.info("route '/showcase' called")
    return FileResponse("./api_rest/showcase/index.html")

@app.get("/assets/{filename}")
async def assets(filename: str):
    logger.info("route '/assets/{}' called".format(filename))
    return FileResponse("./api_rest/showcase/assets/" + filename)
    
restos = {}
with open(RESTOS_FILE, "r") as f:
    restos = json.load(f)

class grade(BaseModel):
    resto: str
    name: str
    grade: conint(ge=1, le=5)
    
@app.get("/restaurants")
def list_restaurants():
    logger.info("route '/restaurants' called")
    return JSONResponse(content=restos)

@app.post("/grade")
def add_grade(grade: grade):
    logger.info("route '/grade' called")
    if grade.resto not in restos:
        restos[grade.resto] = []
    restos[grade.resto].append({grade.name:grade.grade})
    with open(RESTOS_FILE, "w") as f:
        json.dump(restos, f, indent=4)
    return JSONResponse(content=restos)

@app.get("/mean")
def list_mean():
    logger.info("route '/mean' called")
    data = {r: mean(r) for r in restos}
    return JSONResponse(content=data)

@app.get("/restaurants/sort_alpha")
def sort_restaurants():
    logger.info("route '/restaurants/sort_alpha' called")
    data = {r: restos[r] for r in sorted(restos.keys())}
    return JSONResponse(content=data)

@app.get("/restaurants/sort_mean")
def sort_restaurants_mean():
    logger.info("route '/restaurants/sort_mean' called")
    data = {r: restos[r] for r in sorted(restos.keys(), key=lambda x: mean(x), reverse=True)}    
    return JSONResponse(content=data)

# *****************************************************************************
#                  Utility functions
# *****************************************************************************

def mean(r):
    total_sum = sum(next(iter(entry.values())) for entry in restos[r])
    return total_sum / len(restos[r]) if len(restos[r]) > 0 else 0
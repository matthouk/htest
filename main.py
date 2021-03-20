import pandas as pd
import uvicorn
import joblib 
from sklearn.ensemble import RandomForestClassifier
import xgboost 
from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse, Response
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from pydantic import BaseModel
from pydantic import annotated_types

# Creating FastAPI 
app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get('/')
async def root():
    """
    Verifies API is deployed, links to docs
    """ 
    return HTMLResponse("""
    <h1>SKLEARN model API</h1>
    <p>Go to <a href="/docs">/docs</a> for documentation. </p>
    """)


if __name__ == '__main__': 
        uvicorn.run(app, host='127.0.0.1', port=8006)


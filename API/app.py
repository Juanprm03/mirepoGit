import os
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/familia")
def get_family():
    rows = ['Jp', 'Luz', 'George']
    return rows

@app.get("/superheroesDC")
def get_superheroes():
    rows = ['Superman', 'Batman', 'Flash', 'Linterna Verde', 'Aquaman', 'Mujer Maravilla', 'Cyborg', 'Hawkgirl', 'Shazam', 'Green Arrow', 'Black Canary', 'Martian Manhunter']
    return rows
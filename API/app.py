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


@app.get("/superheroesMarvel")
def get_superheroesMarvel():
    rows = ['IroMan', 'Thor', 'Hulk', 'Capitan America', 'SpiderMan', 'Black Widow', 'Doctor Strange', 'AntMan', 'Black Panther', 'Wolverine', 'Deadpool']
    return rows

@app.get("/cursosPlatzi")
def get_cursosPlatzi():
    rows = ['Python', 'JavaScript', 'Java', 'C#', 'PHP', 'Ruby', 'Swift', 'Go', 'Rust']
    return rows
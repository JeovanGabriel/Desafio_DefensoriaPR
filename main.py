from fastapi import FastAPI
import requests
import json

app = FastAPI()
parametro = {"Data Atual":"valor_data"}
requisicao = requests.get("https://testedefensoriapr.pythonanywhere.com/precos", params=parametro)

@app.get("/")
def home():
    return "Insira a data de hoje na url ao lado da / (Ex: DD-MM-AA)"

@app.get("/{data}")
def pegar_data(data: str):
    return requisicao.json()

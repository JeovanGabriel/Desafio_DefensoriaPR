from fastapi import FastAPI
import requests

app = FastAPI()
parametro = {"Data Atual":"valor_data"}
requisicao = requests.get("https://testedefensoriapr.pythonanywhere.com/precos")

@app.get("/")
def home():
    return "Insira a data de hoje na url ao lado da / (Ex: DD-MM-AA)"

@app.get("/{data}")
def pegar_data(data: str):
    if requisicao.status_code == 200:
        return {"Data Atual" : data, "Preços" : requisicao.json()}
    else:
        return "Infelizmente, não conseguimos encontrar os preços, por favor volte mais tarde"

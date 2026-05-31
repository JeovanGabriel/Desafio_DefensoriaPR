#Instalando as bibliotecas
from fastapi import FastAPI
import requests

#Criand a API e a requisição da URL
app = FastAPI()
requisicao = requests.get("https://testedefensoriapr.pythonanywhere.com/precos")

#Texto a mostra na HomePage
@app.get("/")
def home():
    return "Insira a data de hoje na url ao lado da / (Ex: DD-MM-AA)"

#Parametro data
@app.get("/{data}")
def pegar_data(data: str):
    if requisicao.status_code == 200: #Caso o Satus-Code fique em 200 (Indicando que houve contato)
        return {"Data Atual Informada" : data, "Preços" : requisicao.json()}
    else: #Caso o Status-Code seja diferente de 200
        return "Infelizmente, não conseguimos encontrar os preços, por favor volte mais tarde"

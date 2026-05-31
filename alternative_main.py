#Instalando as bibliotecas
from fastapi import FastAPI
import requests
import datetime as dt

#Criando a API e a requisição da URL
alternative_app = FastAPI()
requisicao = requests.get("https://testedefensoriapr.pythonanywhere.com/precos")

#Texto a mostra na HomePage
@alternative_app.get("/")
def home():
    return "Insira (precos) na sua URL para receber os preços atuais dos tapetes"

#sem parametros, apenas a requisição com o "dt.date.today()" usando a nossa data atual 
@alternative_app.get("/precos")
def precos():
    if requisicao.status_code == 200: #Caso o Satus-Code fique em 200 (Indicando que houve contato)
        return {"Data Requisitada" : dt.date.today(), "Preços" : requisicao.json()}
    else: #Caso o Status-Code seja diferente de 200
        return "Infelizmente, não conseguimos encontrar os preços, por favor volte mais tarde"

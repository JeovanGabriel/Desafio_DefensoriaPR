from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def home():
    return "Insira a data de hoje na url ao lado da / (Ex: DD/MM/AA)"
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app = FastAPI()

@app.get("/")
def home():
    return {"hello jajja perro loco": "the world is mine"}

@app.post("/person/new")
def crear_persona():
    pass

par = 'EURUSD'
entrada = 2
direcao = 'call'
timeframe = 1 #apartir de 1 minuto en adelante

status,id = API.buy(entrada, par, direcao, timeframe)

if status:
	resultado,lucro = API.check_win_v3(id)
	
	print('RESULTADO: '+resultado+' / LUCRO: '+str(round(lucro, 2)))
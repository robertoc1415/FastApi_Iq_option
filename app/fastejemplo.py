from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class LoginRequest(BaseModel):
    email: str
    password: str

class TradeRequest(BaseModel):
    type: str
    amount: float
    candle_time: int

def perform_trade(trade_request):
    # Aquí iría la lógica para realizar la operación de compra o venta
    # dependiendo del tipo de par, el monto y el tiempo de vela especificados
    result = "Operación realizada con éxito"
    return result

@app.post("/login")
def login(login_request: LoginRequest):
    # Aquí iría la lógica para verificar que el correo y la contraseña coincidan
    # con algún usuario registrado en la base de datos
    if login_request.email != "user@example.com" or login_request.password != "password":
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    return {"message": "Login successful"}

@app.post("/trade")
def trade(trade_request: TradeRequest):
    result = perform_trade(trade_request)
    return {"message": result}

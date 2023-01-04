from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"hello jajja perro loco": "the world is mine"}

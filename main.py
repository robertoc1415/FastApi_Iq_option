
# from iqoptionapi.stable_api import IQ_Option
# import time, json, datetime, tzlocal
# from dateutil import tz
# #from datetime import datetime as dt
# from datetime import datetime
# from time import time, sleep
# import sys
# import numpy as np
# from talib.abstract import *
# import pandas as pd
# from finta import TA
 
# #Python
# from typing import Optional
# from enum import Enum
# # from email_validator import validate_email

# #Pydantic
# from pydantic import BaseModel 
# from pydantic import Field, PositiveInt , EmailStr



#FastAPI
# from fastapi import FastAPI, Form
from fastapi import FastAPI
# from fastapi import Body, Query, Path

app = FastAPI()

# Models

# class color_cabello(Enum):
#     RED = "RED"
#     GREEN = "GREEN"
#     BLUE = "BLUE"
#     YELLOW = "YELLOW"
#     ORANGE = "ORANGE"
#     PURPLE = "PURPLE"

# class Location(BaseModel): 
#     city: str = Field(...,
#     max_length = 20
#     )
#     state: str = Field(...,
#     min_length= 1
#     )
#     country: str = Field(...,
#     max_length= 1
#     )

# class Person(BaseModel): 
#     first_name: str = Field(...,
#     min_length = 1,
#     max_length = 50,
#     # example = 'roberto'
#     )
#     last_name: str = Field(...,
#     min_length = 1,
#     max_length = 50,
#     # example = 'isajar'
#     )
#     age: int = Field(...,
#     gt = 0,
#     le = 115,
#     # example = 20
#     )
#     hair_color: Optional[color_cabello] = Field(default=None)

#     is_married: Optional[bool] = Field(default=None)

#     premios: int = Field(...,
#     gt = 0,
#     le = 115
#     )
#     email: EmailStr = Field(...)


#     class Config: 
#             schema_extra = {
#                 "example": {
#                     "first_name": "Facundo",
#                     "last_name": "García Martoni",
#                     "age": 21, 
#                     "hair_color": "RED",
#                     "is_married": False,
#                     "premios": 3,
#                     "email": "facundo@gmail.com"
#                 }
#             }

# @app.post("/login")
# def login(email: str = Form(...), password: str = Form(...)):
    # API = IQ_Option(email, password)
    # MODE = "PRACTICE" # PRACTICE / REAL
# API = IQ_Option('roberto.isajar@uao.edu.co', 'Auto3113226598')
    # Verificar la contraseña del usuario aquí (omitido para brevedad)
    # return {"message": "Inicio de sesión exitoso"}
    # return API.connect(),API.change_balance(MODE)
    

@app.get("/")
def home(): 
    return {"Hello": "World"}

# Request and Response Body

# @app.post("/person/new")
# def create_person(
#     person: Person = Body(...)
#     ): 
#     return person

# # Validaciones: Query Parameters

# @app.get("/person/detail")
# def show_person(
#     name: Optional[str] = Query(
#         None,
#         min_length=1,
#         max_length=50,
#         title="Person Name",
#         description="este es el nombre de la persona entre 1 y 50",
#         example="morales"
#         ),
#     age: int = Query(
#         ...,
#         title='edad de persona',
#         description='este es la edad de la persona mayor a 1',
#         example= 3
#         )
# ): 
#     return {name: age}

# # Validaciones: Path Parameters
# @app.get('/person/detail/{person_id}')
# def show_person_detail(
#     person_id: int = Path(..., gt=0 )):
#     return {person_id: 'si existe'}

# # Validaciones: Request Body

# @app.put("/person/{person_id}")
# def update_person(
#     person_id: int = Path(
#         ...,
#         title="Person ID",
#         description="This is the person ID",
#         gt=0,
#         example= 123
#     ),
#     person: Person = Body(...),
#     location: Location = Body(...)

# ): 
#     results = person.dict()
#     results.update(location.dict())
#     return results
#     # return person

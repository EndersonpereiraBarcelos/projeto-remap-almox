from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str 
    
external_data = {
    "username": "Enderson",
    "password": "aaaaa",
}
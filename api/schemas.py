from pydantic import BaseModel


class CreatedUser(BaseModel):
    
    name: str 
    password: chr
    setor: str
    estado: str
    

dados_CreatedUser = {
    "name": "Pokemon",
    "passworld":123456,
    "setor":"Almox",
    "estado":"recife",
}

createduser = CreatedUser(**dados_CreatedUser)

    
##Não sei ao certo 
# class Material(BaseModel):
    
#     setor: str
#     codigo: str
#     material: str
    
    

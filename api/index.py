from fastapi import FastAPI

from schemas import User, external_data

app = FastAPI()
    
# database=[]

@app.get("/api/python")
def hello_world():
    return {"message": "Hello World"}

@app.get("/api/users", response_model=User)
def read_users():
    return {'Users':external_data}



# ##POST 
# @app.get("/api/requisicao")
# def new_requicao():
#     return {"message": "Nova requisição"}

# #GET
# @app.get("/api/criado")
# def criado():
#     return {"message": "Requisição criada"}

# #GET
# @app.get("/api/aprovado")
# def aprovado():
#     return {"message": "Requisição aprovada"}

# ## GetPost
# @app.get("/api/contabilizacao")
# def contabilizacao():
#     return {"message": "Requisição contabilizada"}


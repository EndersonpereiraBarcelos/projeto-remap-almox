from fastapi import FastAPI

app = FastAPI()

@app.get("/api/python")
def hello_world():
    return {"message": "Hello World"}

##POST 
@app.get("/api/requisicao")
def new_requicao():
    return {"message": "Nova requisição"}

#GET
@app.get("/api/criado")
def criado():
    return {"message": "Requisição criada"}

#GET
@app.get("/api/aprovado")
def aprovado():
    return {"message": "Requisição aprovada"}

## GetPost
@app.get("/api/contabilizacao")
def contabilizacao():
    return {"message": "Requisição contabilizada"}


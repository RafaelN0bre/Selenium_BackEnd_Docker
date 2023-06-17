from fastapi import FastAPI

from src.routers import consulta_candidato
app = FastAPI()

app.include_router(consulta_candidato.router)

@app.get("/", tags=["Root"])
def root():
    return {
        "mensagem": "APP IS RUNNING"
    }

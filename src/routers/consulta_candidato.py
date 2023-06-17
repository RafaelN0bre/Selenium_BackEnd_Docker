from fastapi import APIRouter, Response, status
from src.scraps.scrap_consulta_candidato import consulta_candidato

router = APIRouter()

@router.get("/consulta_candidato", status_code=status.HTTP_200_OK)
async def get_candidato(
    response: Response,
    nome_candidato: str
):
    try:
        result = consulta_candidato(nome_candidato)
        response.status_code = status.HTTP_200_OK
        if result:             
            return {
                "message": f"Candidato {nome_candidato} encontrado.",
                "status": response.status_code
            }

        else:
           return {
               "message": "Candidato não Encontrado",
               "status": response.status_code
           }
    except Exception as erro:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            "message": "Erro ao consultar candidato",
            "status": response.status_code,
            "data": str(erro)
        }



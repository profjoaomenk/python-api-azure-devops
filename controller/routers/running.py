from fastapi import APIRouter

router = APIRouter(prefix="")

@router.get("/")
def api_working():
    return "API está rodando."

@router.get("/health")
def api_health():
    return "Saúde da API em dia"
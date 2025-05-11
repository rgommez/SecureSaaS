import logging
from fastapi import APIRouter, Depends
from .auth import get_current_user

logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/secure-endpoint")
def secure_data(user: str = Depends(get_current_user)):
    logger.info(f"Acceso exitoso al endpoint por el usuario: {user}")
    return {"message": f"Hello, {user}. This is a protected endpoint."}

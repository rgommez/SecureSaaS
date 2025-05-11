import logging
from fastapi import FastAPI
from .routes import router as api_router
from prometheus_fastapi_instrumentator import Instrumentator

# Configurar el logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Iniciando SecureSaaS API...")

app = FastAPI(title="SecureSaaS API", docs_url="/docs")

instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

app.include_router(api_router)

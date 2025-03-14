from fastapi import FastAPI
from aiAssistent.app.api.router import router as ai_router
app = FastAPI(openapi_url="/api/v1/assistant/openapi.json", docs_url="/api/v1/assistant/docs")

app.include_router(ai_router)


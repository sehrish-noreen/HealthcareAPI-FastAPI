from fastapi import FastAPI

from src.Healthcare.routes import api_router

version = "v1"
app = FastAPI(version=version)
app.include_router(api_router, prefix=f"/hcapi/{version}")

from fastapi import FastAPI
from app.api.routes import router
from app.db.database import engine, Base
from app.core.config import settings

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.project_name)

app.include_router(router)
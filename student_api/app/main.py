from fastapi import FastAPI
from app.routers import students, healthcheck
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student CRUD API", version="1.0.0")

app.include_router(students.router, prefix="/api/v1")
app.include_router(healthcheck.router, prefix="/api/v1")

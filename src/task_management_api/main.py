from fastapi import FastAPI

from .database import Base, engine
from .models.task import Task
from .routers.tasks import router as task_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Management API",
    description="Backend API built with FastAPI",
    version="1.0.0",
)

app.include_router(task_router)


@app.get("/")
def root():
    return {
        "message": "Task Management API is running",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
    }

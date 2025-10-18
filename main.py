from fastapi import FastAPI
from controller.tasks_controller import router as tasks_router

app = FastAPI(title="Task API - Clean Architecture Example")

app.include_router(tasks_router)

@app.get("/")
def root():
    return {"message": "Task API - up and running"}

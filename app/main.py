from fastapi import FastAPI
from app.routers import tasks, templates

app = FastAPI()

# Register Routers
app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])
app.include_router(templates.router, prefix="/templates", tags=["Templates"])

@app.get("/")
def read_root():
    return {"message": "Welcome to FASTAPI Task Application"}

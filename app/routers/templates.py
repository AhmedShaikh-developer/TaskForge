from fastapi import APIRouter
import json

router = APIRouter()

with open("app/template.json", "r") as f:
    template = json.load(f)

@router.get("/")
def get_template():
    return {"template": template}

@router.post("/")
def fill_template(data: dict):
    return {"message": "Template filled successfully", "data": data}

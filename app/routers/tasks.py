from fastapi import APIRouter, Request, HTTPException
from datetime import datetime

router = APIRouter()

# Mock in-memory database
tasks_db = {}

@router.post("/")
async def create_task(request: Request, task_name: str):
    
    try:
        user = getattr(request.state, "user", None)
        if not user:
            raise HTTPException(status_code=403, detail="User not authenticated")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    username = user.get("username")
    if username not in tasks_db:
        tasks_db[username] = []
        
        
    task = {"task_name": task_name, "created_at": datetime.utcnow()}
    tasks_db[username].append(task)
    
    
    return {"message": "Task created", "task": task}

@router.get("/")
async def get_tasks(request: Request):
    user = getattr(request.state, "user", None)
    if not user:
        raise HTTPException(status_code=403, detail="User not authenticated")

    username = user.get("username")
    tasks = tasks_db.get(username, [])

    return {"tasks": tasks}

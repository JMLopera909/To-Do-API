from datetime import datetime
from fastapi import FastAPI, status
from app.schemas.task import TaskCreate, TaskResponse

app = FastAPI()

tasks = []
next_task_id = 1

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post(
    "/tasks",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_task(task: TaskCreate):
    global next_task_id

    new_task = {
        "id": next_task_id,
        "title": task.title,
        "description": task.description,
        "completed": False,
        "created_at": datetime.now(),
    }

    tasks.append(new_task)

    next_task_id += 1

    return new_task
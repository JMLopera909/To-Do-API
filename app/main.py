from datetime import datetime
from fastapi import FastAPI, HTTPException, status
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate

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

    print(tasks)
    return new_task

@app.get(
    "/tasks",
    response_model=list[TaskResponse],
    status_code=status.HTTP_200_OK,
)
def list_tasks():
    return tasks

@app.put(
    "/tasks/{task_id}",
    response_model=TaskResponse,
    status_code=status.HTTP_200_OK,
)
def update_task(task_id: int, task_update: TaskUpdate):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = task_update.title
            task["description"] = task_update.description
            task["completed"] = task_update.completed

            return task
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Task not found",
    )

@app.delete(
    "/tasks/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(index)
            return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Task not found",
    )
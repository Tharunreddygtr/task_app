from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from . import crud, models, schema
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
    responses={404: {"description": "Not found"}},
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create-task", response_model=schema.Task)
def create_task(task: schema.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db=db, task=task)

@router.get("/{task_id}", response_model=schema.Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.get_task(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

# @router.get("/", response_model=list[schema.Task])
# def read_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#     tasks = crud.get_tasks(db, skip=skip, limit=limit)
#     return tasks

@router.get("/")
def read_tasks(search: str = Query("", description="Search term for title or ID"), db: Session = Depends(get_db)):
    if search:
        tasks = crud.search_tasks(db, search)
    else:
        tasks = crud.get_tasks(db)
    return tasks


@router.put("/{task_id}", response_model=schema.Task)
def update_task(task_id: int, task: schema.TaskUpdate, db: Session = Depends(get_db)):
    db_task = crud.get_task(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return crud.update_task(db=db, task=task)

@router.delete("/{task_id}", response_model=schema.Task)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.delete_task(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task
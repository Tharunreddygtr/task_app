from sqlalchemy.orm import Session
from . import models, schema
from sqlalchemy import or_

def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()



def search_tasks(db: Session, search: str):
    search_lower = search.lower()
    return db.query(models.Task).filter(
        or_(
            models.Task.title.ilike(f'%{search_lower}%'),
            models.Task.id == int(search) if search.isdigit() else None
        )
    ).all()

def get_tasks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Task).order_by(models.Task.id.desc()).offset(skip).limit(limit).all()

def create_task(db: Session, task: schema.TaskCreate):
    db_task = models.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db: Session, task: schema.TaskUpdate):
    db_task = db.query(models.Task).filter(models.Task.id == task.id).first()
    if db_task:
        db_task.title = task.title
        db_task.completed = task.completed
        db.commit()
        db.refresh(db_task)
        return db_task
    return None

def delete_task(db: Session, task_id: int):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if db_task:
        db.delete(db_task)
        db.commit()
        return db_task
    return None

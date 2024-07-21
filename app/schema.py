from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    completed: str

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    id: int

class Task(TaskBase):
    id: int

    class Config:
        from_attributes = True
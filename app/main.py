from fastapi import FastAPI
from . import models, database
from fastapi.middleware.cors import CORSMiddleware
from . import task

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

app.include_router(task.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

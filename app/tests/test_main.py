# app/tests/test_main.py

from fastapi.testclient import TestClient
from app.main import app
from app.database import SessionLocal, engine
from app.models import Base

# Create a TestClient instance
client = TestClient(app)

# Setup and teardown for database
def setup_module(module):
    # Create the database tables
    Base.metadata.create_all(bind=engine)

def teardown_module(module):
    # Drop the database tables
    Base.metadata.drop_all(bind=engine)

def test_create_task():
    response = client.post(
        "/tasks/create-task",
        json={"title": "Test Task", "completed": "Pending"}
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"
    assert response.json()["completed"] == "Pending"

def test_read_task():
    # Create a task to read
    client.post(
        "/tasks/create-task",
        json={"title": "Test Task", "completed": "Pending"}
    )
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert response.json()[0]["title"] == "Test Task"

def test_update_task():
    # Create a task to update
    response = client.post(
        "/tasks/create-task",
        json={"title": "Update Test Task", "completed": "Pending"}
    )
    task_id = response.json()["id"]

    response = client.put(
        f"/tasks/{task_id}",
        json={"id": task_id ,"title": "Updated Task Title", "completed": "In Progress"}
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Task Title"
    assert response.json()["completed"] == "In Progress"

def test_delete_task():
    # Create a task to delete
    response = client.post(
        "/tasks/create-task",
        json={"title": "Delete Test Task", "completed": "Pending"}
    )
    task_id = response.json()["id"]

    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200

    # Verify the task is deleted
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 404

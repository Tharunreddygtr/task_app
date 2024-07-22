# Task List Application

This is a task list application built with FastAPI for the backend and React.js for the frontend. 
It includes features for creating, reading, updating, and deleting tasks.


## Technologies Used

- **Backend:**
  - FastAPI
  - SQLAlchemy
  - Pydantic
  - Uvicorn
  - Alembic (for migrations)

- **Frontend:**
  - React.js
  - Axios for API calls
  - Bootstrap for styling

## Installation and Setup

### Backend

1. **Clone the repository:**

    ```sh
    git clone https://github.com/Tharunreddygtr/task_app.git
    cd task_app
    ```

2. **Create a virtual environment and activate it:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the database:**

    - Make sure you have MySQL installed and running.
    - Create a database named `taskdb`.

    ```sh
    mysql -u root -p
    CREATE DATABASE taskdb;
    ```

5. **Configure the database URL in `app/database.py`:**

    ```python
    SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:yourpassword@localhost:3306/taskdb"
    ```

6. **Run Alembic migrations to create the tables:**

    ```sh
    alembic init alembic
    ```

    - Configure `alembic.ini`:

    ```ini
    sqlalchemy.url = mysql+mysqlconnector://root:yourpassword@localhost/taskdb
    ```

    - Create the initial migration:

    ```sh
    alembic revision --autogenerate -m "Initial migration"
    alembic upgrade head
    ```

7. **Run the FastAPI server:**

    ```sh
    uvicorn app.main:app --reload
    ```

### Frontend

1. **Navigate to the `frontend` directory:**

    ```sh
    cd frontend
    ```

2. **Install the dependencies:**

    ```sh
    npm install
    ```

3. **Start the React development server:**

    ```sh
    npm start
    ```

### Running the Project

- The backend will be running on `http://localhost:8000`.
- The frontend will be running on `http://localhost:3000`.

### API Documentation

- You can access the automatically generated API documentation at `http://localhost:8000/docs`.

### Unit Tests

1. **Run the tests:**

    ```sh
    pytest
    ```








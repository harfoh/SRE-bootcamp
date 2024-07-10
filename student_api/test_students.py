from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine, get_db
from sqlalchemy.orm import sessionmaker
from app.models import Student

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_create_student():
    response = client.post("/api/v1/students/", json={"name": "John Doe", "age": 20, "grade": "A"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "John Doe"
    assert data["age"] == 20
    assert data["grade"] == "A"
    assert "id" in data

def test_read_students():
    response = client.get("/api/v1/students/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_read_student():
    response = client.post("/api/v1/students/", json={"name": "Jane Doe", "age": 21, "grade": "B"})
    assert response.status_code == 200
    student_id = response.json()["id"]
    
    response = client.get(f"/api/v1/students/{student_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Jane Doe"
    assert data["age"] == 21
    assert data["grade"] == "B"
    assert data["id"] == student_id

def test_update_student():
    response = client.post("/api/v1/students/", json={"name": "Alice", "age": 22, "grade": "C"})
    assert response.status_code == 200
    student_id = response.json()["id"]

    response = client.put(f"/api/v1/students/{student_id}", json={"name": "Alice Updated", "age": 23, "grade": "B+"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Alice Updated"
    assert data["age"] == 23
    assert data["grade"] == "B+"

def test_delete_student():
    response = client.post("/api/v1/students/", json={"name": "Bob", "age": 23, "grade": "B"})
    assert response.status_code == 200
    student_id = response.json()["id"]

    response = client.delete(f"/api/v1/students/{student_id}")
    assert response.status_code == 200

    response = client.get(f"/api/v1/students/{student_id}")
    assert response.status_code == 404

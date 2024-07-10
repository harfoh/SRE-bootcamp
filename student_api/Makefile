install:
    pip install -r requirements.txt

migrate:
    alembic upgrade head

run:
    uvicorn app.main:app --reload

test:
    pytest

install:
    pip install -r requirements.txt

migrate:
    alembic upgrade head

run:
    uvicorn app.main:app --reload

test:
    pytest


IMAGE_NAME=api:v1.0
CONTAINER_NAME=student-api
PORT=8000

# Phony targets
.PHONY: install migrate run test build_docker run_docker stop_docker

# Install dependencies
install:
	pip install -r requirements.txt

# Run database migrations
migrate:
	alembic upgrade head

# Run the FastAPI application locally
run:
	uvicorn app.main:app --reload

# Run tests
test:
	pytest

# Build the Docker image
build_docker:
	docker build -t $(IMAGE_NAME) .

# Run the Docker container
run_docker: stop_docker
	docker run -d -p $(PORT):$(PORT) --name $(CONTAINER_NAME) $(IMAGE_NAME)

# Stop the Docker container
stop_docker:
	-docker stop $(CONTAINER_NAME)
	-docker rm $(CONTAINER_NAME)

# Rebuild and run the Docker container
restart_docker: build_docker run_docker


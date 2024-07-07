# Use the official Ubuntu image
FROM ubuntu:22.04

# Set the working directory in the container
WORKDIR /app

# Install dependencies and Python 3
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    curl \
    bash \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to the PATH
ENV PATH="/root/.local/bin:$PATH"

# Copy the rest of the application code into the container
COPY . /app

# Install the dependencies using Poetry
RUN poetry install

# Make sure the prestart script is executable
RUN chmod +x ./prestart.sh

RUN tr -d '\r' < prestart.sh > prestart_fixed.sh \
    && mv prestart_fixed.sh prestart.sh
    
# Set environment variables
ENV PYTHONPATH=/app

# Expose the port the app runs on
EXPOSE 8000

# Print Python and Poetry version for debugging
RUN python3 --version && poetry --version

# Run the prestart script and then start the Uvicorn server
CMD ["bash", "-c", "poetry run bash ./prestart.sh && poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000"]


# Use the official Python image as the base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install build-essential for compilation
RUN apt-get update && apt-get install -y build-essential && \
    pip install poetry && \
    apt-get purge -y build-essential && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install poetry

# Copy poetry files first to leverage caching
COPY pyproject.toml poetry.lock ./

# Disable Poetry virtualenvs
RUN poetry config virtualenvs.create false

# Install dependencies
RUN poetry install --no-interaction --no-ansi --no-root


# Copy the entire project
COPY . .

# Run the app
CMD ["poetry", "run", "python3", "__main__.py"]



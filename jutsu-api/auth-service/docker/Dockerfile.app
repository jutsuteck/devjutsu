# This sets the base image for the Docker container, in this case, it's the official image for Python 3.10 with slim-buster (Debian) as the operating system
FROM python:3.10-slim-buster

# These are argument variables, used to define and pass values during the Docker build
ARG POSTGRES_USER
ARG POSTGRES_PASSWORD
ARG POSTGRES_HOST
ARG POSTGRES_PORT
ARG POSTGRES_DB

# Here we're taking the argument variables and defining them as environment variables in the container.
# The environment variables can be accessed by the application to configure database settings.
ENV POSTGRES_USER=${POSTGRES_USER}
ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
ENV POSTGRES_HOST=${POSTGRES_HOST}
ENV POSTGRES_PORT=${POSTGRES_PORT}
ENV POSTGRES_DB=${POSTGRES_DB}

# These environment variables are specific to Python.
# PYTHONDONTWRITEBYTECODE prevents Python from creating .pyc files.
# PYTHONUNBUFFERED keeps Python from buffering the standard output (important for logging)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory to /app. All the following instructions (like RUN, CMD, ADD, COPY) will be run from this path in the container.
WORKDIR /app

# This copies the Pipfile and Pipfile.lock from the local directory (on the host) into the Docker container.
COPY Pipfile Pipfile.lock /app/

# This installs pipenv and then the Python dependencies from the Pipfile.
RUN pip install pipenv && pipenv install --system

# This copies the src directory (and all its subdirectories) from your project into the Docker container.
COPY src /app/src

# Creates a new user named 'ghostfist' and set its home directory to /home/ghostfist.
RUN useradd -m ghostfist

# Switch to 'ghostfist' user for executing subsequent commands for security reasons (i.e., not running the container as the root user).
USER ghostfist

# This is the command that will be run when the Docker container is started.
# In this case, it starts the FastAPI application with Uvicorn, listening on all interfaces at port 8000 and in reload mode.
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

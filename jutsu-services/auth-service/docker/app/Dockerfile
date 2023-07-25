FROM python:3.10-slim-buster

# Define the environment
ARG ENVIRONMENT
ENV ENVIRONMENT=${ENVIRONMENT}

# # These are argument variables, used to define and pass values during the Docker build
# ARG POSTGRES_USER
# ARG POSTGRES_HOST
# ARG POSTGRES_PORT
# ARG POSTGRES_DB

# # Here we're taking the argument variables and defining them as environment variables in the container.
# # The environment variables can be accessed by the application to configure database settings.
# ENV POSTGRES_USER=${POSTGRES_USER}
# ENV POSTGRES_HOST=${POSTGRES_HOST}
# ENV POSTGRES_PORT=${POSTGRES_PORT}
# ENV POSTGRES_DB=${POSTGRES_DB}

# These environment variables are specific to Python.
# PYTHONDONTWRITEBYTECODE prevents Python from creating .pyc files.
# PYTHONUNBUFFERED keeps Python from buffering the standard output (important for logging)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY scripts/startup.sh /app/scripts/

COPY alembic /app/alembic

COPY alembic.ini /app/

COPY src /app/src

COPY Pipfile Pipfile.lock /app/

# Update system packages and cleanup
RUN apt-get update && apt-get upgrade -y && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

RUN pip install pipenv && pipenv install --system

# Create a user with a specific UID and GID
RUN groupadd -g 999 ghostfist && useradd -r -u 999 -g ghostfist ghostfist

USER ghostfist

CMD ["./scripts/startup.sh"]


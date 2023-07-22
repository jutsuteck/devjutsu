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

WORKDIR /app

COPY startup.sh /app/

COPY alembic /app/alembic

COPY alembic.ini /app/

COPY src /app/src

COPY Pipfile Pipfile.lock /app/

RUN pip install --upgrade pip

RUN pip install pipenv && pipenv install --system

RUN useradd -m ghostfist

USER ghostfist

CMD ["./startup.sh"]

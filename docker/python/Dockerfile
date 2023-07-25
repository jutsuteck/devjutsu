FROM python:3.10-slim-buster

# Define the environment
ARG ENVIRONMENT
ENV ENVIRONMENT=${ENVIRONMENT}

# These environment variables are specific to Python.
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

WORKDIR /app

# Update system packages and cleanup
RUN apt update && \
    apt upgrade -y && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

# Create a user with a specific UID and GID
RUN groupadd -g 999 appuser && useradd -r -u 999 -g appuser appuser

# Switch to the new user
USER appuser

# Copy the Pipfile and Pipfile.lock
COPY --chown=appuser:appuser jutsu-services/auth-service/Pipfile jutsu-services/auth-service/Pipfile.lock /app/

# Copy the other necessary files and directories
COPY --chown=appuser:appuser jutsu-services/auth-service/scripts/startup.sh /app/scripts/
COPY --chown=appuser:appuser jutsu-services/auth-service/alembic /app/alembic
COPY --chown=appuser:appuser jutsu-services/auth-service/alembic.ini /app/
COPY --chown=appuser:appuser jutsu-services/auth-service/src /app/src

# Install pipenv as root, then switch back to appuser
USER root
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --system --deploy
USER appuser


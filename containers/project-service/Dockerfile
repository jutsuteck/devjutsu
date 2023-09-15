FROM python:3.11.4-alpine

# Define the environment
ARG ENVIRONMENT
ENV ENVIRONMENT=${ENVIRONMENT}

# These environment variables are specific to Python.
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

WORKDIR /app

# Update system packages, install bash and cleanup
RUN apk update && \
    apk upgrade && \
    apk add --no-cache bash && \
    rm -rf /var/cache/apk/*

# Create a user with a specific UID and GID
RUN addgroup appuser && adduser -D -u 999 -G appuser appuser

# Switch to the new user
USER appuser

# Copy the Pipfile and Pipfile.lock
COPY --chown=appuser:appuser jutsu-services/project-service/Pipfile jutsu-services/project-service/Pipfile.lock /app/

# Copy the other necessary files and directories
COPY --chown=appuser:appuser jutsu-services/project-service/scripts/startup.sh /app/scripts/
# COPY --chown=appuser:appuser jutsu-services/project-service/alembic /app/alembic
# COPY --chown=appuser:appuser jutsu-services/project-service/alembic.ini /app/
COPY --chown=appuser:appuser jutsu-services/project-service/src /app/src

# Install pipenv as root, then switch back to appuser
USER root
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --system --deploy
USER appuser

# This Dockerfile is used to build an image for the auth-service of the 'jutsu' project.
# 
# Owner: JutsuTeck
# Email: imanuelfebie@devjutsu.io
# 
# This Dockerfile is based on the Python 3.10 slim-buster image. It sets up the environment and
# system packages, then creates a specific user with appropriate permissions for our use case.
# 
# The working directory is set to /app and necessary files and directories are copied into it.
# Pipenv is installed and dependencies are managed with it.
# 
# Note: The ENVIRONMENT argument can be set at build time to specify the deployment context.
#
# Please reach out to the owner before making significant changes.
#
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

# Install pipenv as root, then switch back to appuser
USER root
RUN pip install --upgrade pip
RUN pip install pipenv
USER appuser


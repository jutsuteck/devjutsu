FROM python:3.11.4-alpine

# Define the environment
ARG ENVIRONMENT
ENV ENVIRONMENT=${ENVIRONMENT}

# These environment variables are specific to Python.
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1


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


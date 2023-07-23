#!/bin/sh

# Navigate to the app directory
cd /app

# Run the database migrations using Alembic
echo "Running database migrations..."
alembic upgrade head

# Start the Uvicorn server
echo "Starting Uvicorn server..."
exec uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload

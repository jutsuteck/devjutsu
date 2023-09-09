#!/usr/bin/env bash

# Navigate to the app directory
cd /app || exit

# Run the database migrations using Alembic
echo "Running database migrations..."
alembic upgrade head || { echo "Migrations failed" ; exit 1; }

echo "Seeding the database with default roles and permissions..."
python3 -m scripts.seed_database

# Start the Uvicorn server
echo "Starting Uvicorn server..."
exec uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload

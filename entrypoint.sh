#!/bin/bash
set -e

echo "Waiting for PostgreSQL..."
while ! pg_isready -h "$POSTGRES_HOST" -U "$POSTGRES_USER"; do
    sleep 1
done

echo "Starting server..."
exec python manage.py runserver 0.0.0.0:8000

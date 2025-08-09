#!/bin/bash
set -e

echo "Waiting for PostgreSQL..."
until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$POSTGRES_HOST" -U "$POSTGRES_USER" -d "postgres" -c '\q'; do
  sleep 1
done

echo "Creating database if not exists..."
PGPASSWORD=$POSTGRES_PASSWORD psql -h "$POSTGRES_HOST" -U "$POSTGRES_USER" -d "postgres" -c "CREATE DATABASE \"$POSTGRES_DB\";" || echo "Database already exists"

echo "Starting server..."
exec python manage.py runserver 0.0.0.0:8000

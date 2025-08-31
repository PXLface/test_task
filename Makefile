DC = docker compose

APP_FILE = docker_compose/app.yaml
APP_CONTAINER = main-app

STORAGES_FILE = docker_compose/storages.yaml
DB_CONTAINER = postgres-db

ENV = --env-file .env
MANAGE_PY = python manage.py

LOGS = docker logs
EXEC = docker exec -it

.PHONY: storages_up
storages_up:
	${DC} -f ${STORAGES_FILE} ${ENV} up -d

.PHONY: storages_down
storages_down-down:
	${DC} -f ${STORAGES_FILE} down

.PHONY: app_logs
app_logs:
	${LOGS} ${APP_CONTAINER} -f

.PHONY: app_up
app_up:
	${DC} -f ${APP_FILE} -f ${STORAGES_FILE} ${ENV} up --build -d

.PHONY: app_up_no_build
app_up_no_build:
	${DC} -f ${APP_FILE} -f ${STORAGES_FILE} ${ENV} up -d

.PHONY: app_down
app_down:
	${DC} -f ${APP_FILE} -f ${STORAGES_FILE} down

.PHONY: makemigrations
makemigrations:
	${EXEC} ${APP_CONTAINER} ${MANAGE_PY} makemigrations

.PHONY: migrate
migrate:
	${EXEC} ${APP_CONTAINER} ${MANAGE_PY} migrate

.PHONY: superuser
superuser:
	${EXEC} ${APP_CONTAINER} ${MANAGE_PY} createsuperuser

.PHONY: run_test
run_test:
	${EXEC} ${APP_CONTAINER} pytest

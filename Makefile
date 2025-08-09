DC = docker compose
ENV = --env-file .env
DB_CONTAINER = postgresql_db
STORAGES_FILE = docker_compose/storages.yaml
APP_FILE = docker_compose/app.yaml
LOGS = docker logs
APP_CONTAINER = main-app
EXEC = docker exec -it
MANAGE_PY = python manage.py

.PHONY: app-start
app-start:
	${DC} -f ${APP_FILE} -f ${STORAGES_FILE} ${ENV} up --build -d

.PHONY: app-logs
app-logs:
	${LOGS} ${APP_CONTAINER} -f

.PHONY: app-down
app-down:
	${DC} -f ${APP_FILE} -f ${STORAGES_FILE} down

.PHONY: migrate
migrate:
	${EXEC} ${APP_CONTAINER} ${MANAGE_PY} migrate

.PHONY: migrations
migrations:
	${EXEC} ${APP_CONTAINER} ${MANAGE_PY} makemigrations

.PHONY: superuser
superuser:
	${EXEC} ${APP_CONTAINER} ${MANAGE_PY} createsuperuser

.PHONY: collectstatic
collectstatic:
	${EXEC} ${APP_CONTAINER} ${MANAGE_PY} collectstatic

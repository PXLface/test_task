DC = docker compose
ENV = --env-file .env
DB_CONTAINER = postgresql_db
STORAGES_FILE = docker_compose/storages.yaml
APP_FILE = docker_compose/app.yaml
LOGS = docker logs
APP_CONTAINER = main-app



.PHONY: app-start
app-start:
	$(DC) -f $(APP_FILE) -f $(STORAGES_FILE) $(ENV) up -d

.PHONY: app-logs
app-logs:
	${LOGS} ${APP_CONTAINER} -f

.PHONY: app-down
app-down:
	${DC} -f ${APP_FILE} -f ${STORAGES_FILE} down

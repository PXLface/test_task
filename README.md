# Web-service for Cash Flow Managment

> Web app, which allows users to crate, edit, delete and view cash flow records

---

## 📥 Clone the repository:

```
git clone https://github.com/your_username/your_repository.git
cd your_repository
```

---

## 📦 Install requirements

1. Install [Docker][Web app, which allows users to crate, edit, delete and view cash flow records]
2. If Docker version is less than 23.0 than install [Docker-compose][https://docs.docker.com/compose/install/]
3. Install [GNU Make][https://www.gnu.org/software/make/] for convenience

---

## ⚙️ Database and project settings

- All environment variables are in the file `.env`
```
# Django
DJANGO_SECRET_KEY=djangosecretkey
DJANGO_PORT=8000

# PostgreSQL
POSTGRES_DB=yourdb
POSTGRES_USER=youruser
POSTGRES_PASSWORD=yourpassword
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
```
- To develop a Django project, use the settings inside the file. `core/project/settings/local.py`

---

## 🚀 Launching a web service

- ✅ Using GNU Make:
```
make app-up
```
- ⚠️ Without GNU Make
```
docker compose -f docker_compose/app.yaml -f docker_compose/storages.yaml --env-file .env up --build -d
```

---

## 🔧 Frequently used commands

### App commands

#### Stream application container logs
(Make) `make app-logs`
(Docker) `docker logs main-app -f`
#### Stop all containers and networks
(Make) `make app-down`
(Docker) `docker compose -f docker_compose/app.yaml -f docker_compose/storages.yaml down`

### Django operations

#### Make migrations to models
(Make) `make migrations`
(Docker) `docker exec -it main-app python manage.py makemigrations`

#### Apply pending migrations to database
(Make) `make migrate`
(Docker) `docker exec -it main-app python manage.py migrate`

#### Create Django admin account
(Make) `make superuser`
(Docker) `docker exec -it main-app python manage.py createsuperuser`

#### Gather static files in production location
(Make) `make collectstatic`
(Docker) `docker exec -it main-app python manage.py collectstatic`

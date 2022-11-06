# Viboo
Setup to run api:
 - Install Docker Desktop -> https://www.docker.com/products/docker-desktop/
 - In Repository root run: 1) remove data diretory and run `docker compose build` 2) `docker compose up —wait db` 3) `docker compose up` 4) open a new terminal window and run `docker-compose exec web python manage.py makemigrations --noinput` and `docker-compose exec web python manage.py migrate --noinput` 5) close all the windows and run `docker compose down` and `docker compose up` 
 - After this setup you just need to run the api a simple command: `docker compose up`and to stop `docker compose down`

Postman Collections with samples requests: https://www.getpostman.com/collections/1b94ce3eac5a9bed2283

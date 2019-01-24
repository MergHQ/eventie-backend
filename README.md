# Eventie

Backend for eventie, a event calendar and enrollment system, made in python.

### Setting up a devenv

For setting up a development environment, you need docker, docker compose and a postgres database.

1. Opent the docker-compose.yml file and edit the environemnt variables to match your database configuration.
3. run `docker-compose run web npm run migrate-latest`
4. run `docker-compose up`
5. ???
6. go to `localhost:4200`
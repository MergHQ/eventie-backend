# Eventie

Backend for eventie, a event calendar and enrollment system, made in python.

[Link to frontend](https://github.com/MergHQ/eventie-frontend)
[Link to application](http://eventie-frontend.herokuapp.com/)

### Setting up a devenv

For setting up a development environment, you need docker, docker compose and a postgres database.

1. Open the docker-compose.yml file and edit the environment variables to match your database configuration.
3. run `docker-compose run web npm run migrate-latest`
4. run `docker-compose up`
5. ???
6. go to `localhost:4200`

[Tietokantakaavio](/docs/database.md)
[Käyttötapaukset](/docs/docs.md)

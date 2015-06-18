# Python Club

Colaborative blog system

## Development

### Via Docker

Developing via Docker will give you all infrastructure needed for project
already configured and guarantees that everyone involved in the project
will have the same environment.

You'll need to install `Docker` and `docker-compose` before proceed.

Create `.env` file from template

    $ cp .env-example .env

Build the containers

    $ docker-compose build

To run use

    $ docker-compose up

Then access http://localhost:8000/

To run any command inside of a container use

    $ docker-compose run [container_name] [command]

Example:

    $ docker-compose run web python manage.py shell


### The hard way

Create `.env` file from template

    $ cp .env-example .env

Create a database from proejct and adjust `DATABASE_URL` on `.env` file

    $ vim .env

And run server

    $ python manage.py runserver

Then access http://localhost:8000/

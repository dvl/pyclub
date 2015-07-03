# Python Club

Colaborative blog system

This project has the intention to replace the current system used on
[pythonclub.com.br](http://pythonclub.com.br) a blog where everyone has
access to post anything related with Python (and web development in general)
just using your GitHub account.

All posts and editions must be approved by a staff member before appears online.

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
    
Install migrations:

    $ docker-compose run web python manage.py migrate
    
And you also may need to create a superuser:

    $ docker-compose run web python manage.py createsuperuser

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

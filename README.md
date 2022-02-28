# FastAPI (Example): pokeapi

Example application when implementing an api rest server with the FastAPI framework, Docker and PostgreSQL.

## Model

[![](https://mermaid.ink/img/pako:eNqtUsuKwzAM_BWjc_sDvnXZHMI-WkguC4EgYm1qNrGLI1NKyL-vY7JpAulpq5M0zIzEoB4qqwgkkHvVWDtsCyOmOh3fko_jZyYGu9_bXuRfpySTM1zG-TE9yw_5kh7nx_TDS_qe5ulqw4xtyPo7NpY2TDU5odUa79hpUwuDLW0LrqTrM2-KGlsha2tKdIQlmcr6IHLdmqyQiXVLosGOy8qazjdMizOGexsj-9fpC7MY6LPM5qifZTgW7KAl16JW4cOibwF8pqAAGVqF7qeAwgyB5y9jjonSbB3Ib2w62gF6ttnNVCDZefojTY86sYZfYqnEUQ)](https://mermaid.live/edit#pako:eNqtUsuKwzAM_BWjc_sDvnXZHMI-WkguC4EgYm1qNrGLI1NKyL-vY7JpAulpq5M0zIzEoB4qqwgkkHvVWDtsCyOmOh3fko_jZyYGu9_bXuRfpySTM1zG-TE9yw_5kh7nx_TDS_qe5ulqw4xtyPo7NpY2TDU5odUa79hpUwuDLW0LrqTrM2-KGlsha2tKdIQlmcr6IHLdmqyQiXVLosGOy8qazjdMizOGexsj-9fpC7MY6LPM5qifZTgW7KAl16JW4cOibwF8pqAAGVqF7qeAwgyB5y9jjonSbB3Ib2w62gF6ttnNVCDZefojTY86sYZfYqnEUQ)
## Dependencies
- [Docker](https://www.docker.com/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [PostgreSQL](https://www.postgresql.org/)

## How to use it

Create the **.env** file in the root folder indicating each of the environment variables


```
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=db_name
PGADMIN_DEFAULT_EMAIL=email
PGADMIN_DEFAULT_PASSWORD=pgadmin_password
```

We install the libraries and the initial configuration of the containers.

```bash 
$ docker-compose build
```
the model is migrated to the database
```bash 
$ docker-compose run app alembic upgrade head
```
and the servers are started
```bash 
$ docker-compose up
```
Use the following address to consult end points, diagrams, etc.
```bash 
$ http://localhost/docs
```
## Tests
To perform the tests run the following command
```bash 
$ docker-compose run app pytest
```
## License
[MIT](https://choosealicense.com/licenses/mit/)
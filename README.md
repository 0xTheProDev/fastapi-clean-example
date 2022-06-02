# fastapi-example

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://docs.python.org/3/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![OpenAPI](https://img.shields.io/badge/openapi-6BA539?style=for-the-badge&logo=openapi-initiative&logoColor=fff)](https://www.openapis.org/)
[![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)](https://swagger.io/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge)](https://black.readthedocs.io/en/stable/)
[![Typed with: pydantic](https://img.shields.io/badge/typed%20with-pydantic-BA600F.svg?style=for-the-badge)](https://black.readthedocs.io/en/stable/)
[![Open Issues](https://img.shields.io/github/issues-raw/Progyan1997/fastapi-example?style=for-the-badge)](https://github.com/Progyan1997/fastapi-example/issues)
[![Closed Issues](https://img.shields.io/github/issues-closed-raw/Progyan1997/fastapi-example?style=for-the-badge)](https://github.com/Progyan1997/fastapi-example/issues?q=is%3Aissue+is%3Aclosed)
[![Open Pulls](https://img.shields.io/github/issues-pr-raw/Progyan1997/fastapi-example?style=for-the-badge)](https://github.com/Progyan1997/fastapi-example/pulls)
[![Closed Pulls](https://img.shields.io/github/issues-pr-closed-raw/Progyan1997/fastapi-example?style=for-the-badge)](https://github.com/Progyan1997/fastapi-example/pulls?q=is%3Apr+is%3Aclosed)
[![Contributors](https://img.shields.io/github/contributors/Progyan1997/fastapi-example?style=for-the-badge)](https://github.com/Progyan1997/fastapi-example/graphs/contributors)
[![Activity](https://img.shields.io/github/last-commit/Progyan1997/fastapi-example?style=for-the-badge&label=most%20recent%20activity)](https://github.com/Progyan1997/fastapi-example/pulse)

## Description

_Example Application Interface using FastAPI framework in Python 3_

This example showcases Repository Pattern in Hexagonal Architecture _(also known as Clean Architecture)_. Here we have two Entities - Books and Authors, whose relationships have been exploited to create CRUD endpoint in REST under OpenAPI standard.

## Installation

- Install all the project dependency using [Pipenv](https://pipenv.pypa.io):

  ```sh
  $ pipenv install --dev
  ```

- Run the application from command prompt:
  ```sh
  $ pipenv run uvicorn main:app --reload
  ```
- Open `localhost:8000/docs` for API Documentation

## Testing

For Testing, `unittest` module is used for Test Suite and Assertion, whereas `pytest` is being used for Test Runner and Coverage Reporter.

- Run the following command to initiate test:
  ```sh
  $ pipenv run pytest
  ```
- To include Coverage Reporting as well:
  ```sh
  $ pipenv run pytest --cov-report xml --cov .
  ```

## License

&copy; MIT License

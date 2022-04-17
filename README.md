# fastapi-example

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)
![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge)

## Description

_Example Application Interface using FastAPI framework in Python 3_

This example showcases Repository Pattern in Hexagonal Architecture _(also known as Clean Architecture)_. Here we have two Entities - Books and Authors, whose relationships have been exploited to create CRUD endpoint in REST under OpenAPI standard.

## Installation

- Create and activate a Virtual Environment for Python 3 in your workspace:

  ```sh
  $ python3 -m venv env
  $ source venv/bin/activate
  ```

- Install all the project dependency using Pip:

  ```sh
  $ pip install -r requirements.txt
  ```

- Run the application from command prompt:
  ```sh
  $ uvicorn main:app --reload
  ```
- Open `localhost:8000/docs` for API Documentation

## License

&copy; MIT License

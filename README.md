# To-Do API Professional

A professional backend project built with FastAPI, PostgreSQL, SQLAlchemy, Alembic, and Docker.

## Objective

The purpose of this project is to simulate the development of a real-world backend service while applying professional software engineering practices.

## Tech Stack

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy 2.0
* Alembic
* Pydantic
* Docker
* Docker Compose
* Git & GitHub

## Features

Current features:

* Health check endpoint

Planned features:

* Task management CRUD
* PostgreSQL persistence
* Database migrations
* Dockerized deployment
* Testing
* API documentation
* Authentication and authorization
* Advanced filtering and pagination

## Requirements

* Python 3.12+
* PostgreSQL
* Docker
* Git

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd To-Do-API
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the API

Start the application:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

## Current Endpoint

### Health Check

```http
GET /health
```

Response:

```json
{
  "status": "ok"
}
```

## Project Structure

```text
to-do-api/
│
├── app/
│   ├── core/
│   └── main.py
│
├── tests/
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Development Status

Current Phase: Phase 0 — Environment Setup

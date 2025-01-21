# Todo API

This project is a simple Todo API built with Flask, following a clean architecture approach. It includes endpoints to create, read, update, and delete todo items:

`GET /api/todo/<int:todo_id>`: Retrieve a todo item by ID.

`PUT /api/todo/<int:todo_id>`: Create a new todo item.

`PATCH /api/todo/<int:todo_id>`: Update an existing todo item.

`DELETE /api/todo/<int:todo_id>`: Delete a todo item by ID.

## Getting Started

### Prerequisites

- Docker
- Python 3.7+
- pip (Python package installer)

### Installation

1. Clone the repository:

   ```bash
   git clone git@github.com:manuel-io/sample-python-flask-api.git
   cd sample-python-flask-api
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv

   # Activate env on MacOS/Linux
   source venv/bin/activate

   # On Windows use
   venv\Scripts\activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:

   ```bash
   # For local development
   FLASK_APP=run.py
   FLASK_ENV=development
   DATABASE_URL=sqlite:///database.db
   API_URL=http://127.0.0.1:5000/api
   ```

### Running the Project

#### Run locally

```bash
python run.py
```

#### Serve a production ready version locally

```bash
gunicorn --bind 0.0.0.0:8000 wsgi:app
```

The API will be available at `http://127.0.0.1:8000/api` and Swagger UI will be available at `http://127.0.0.1:8000/api/swagger`.

#### Run the application using Docker

```bash
docker build -t todo-api .
```

```bash
docker run -d -p 8000:8000 --name todo-api-container todo-api
```

The API will be available at `http://127.0.0.1:8000/api` and Swagger UI will be available at `http://127.0.0.1:8000/api/swagger`.

### Running Tests

#### Unit Tests

To run unit tests, use the following command:

```bash
python -m unittest discover -s tests/unit
```

### Integration Tests

To run integration tests, use the following command:

```bash
python -m unittest discover -s tests/integration
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

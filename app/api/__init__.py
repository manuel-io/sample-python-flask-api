from flask import Blueprint
from flask_restx import Api

# Create a Blueprint for the API
api_bp = Blueprint('api', __name__)

# Create an Api object with additional metadata
api = Api(
    api_bp,
    version='1.0',
    title='Todo API',
    description='A simple Todo API',
    doc='/swagger'  # Swagger UI endpoint
)

# Import and add namespaces
from .todo import api as todo_ns
api.add_namespace(todo_ns, path='/todos')
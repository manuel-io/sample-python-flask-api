from flask_restx import fields, reqparse

todo_resource_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'description': fields.String,
    'completed': fields.Boolean
}

todo_model = {
    'title': fields.String(required=True, description='Title of the todo'),
    'description': fields.String(description='Description of the todo'),
    'completed': fields.Boolean(required=True, description='Completion status of the todo')
}

todo_update_args = reqparse.RequestParser()
todo_update_args.add_argument("title", type=str, help="Title of the todo")
todo_update_args.add_argument("description", type=str, help="Description of the todo")
todo_update_args.add_argument("completed", type=bool, help="Completion status of the todo")
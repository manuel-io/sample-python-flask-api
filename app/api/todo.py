from flask_restx import Namespace, Resource, marshal_with, abort
from . import api
from app.services.todo_service import TodoService
from app.domain.schemas.todo_schema import todo_resource_fields, todo_model, todo_update_args

api = Namespace('todos', description='Todo operations')

@api.route('/todo/<int:todo_id>')
class TodoResource(Resource):
    @marshal_with(todo_resource_fields)
    def get(self, todo_id):
        result = TodoService.get_todo(todo_id)
        if not result:
            abort(404, message="Todo not found")
        return result

    @api.expect(api.model('Todo', todo_model))
    @marshal_with(todo_resource_fields)
    def put(self, todo_id):
        args = todo_update_args.parse_args()
        todo = TodoService.get_todo(todo_id)
        if not todo:
            abort(404, message="Todo not found")
        todo = TodoService.update_todo(todo, args['title'], args['description'], args['completed'])
        return todo, 200

    def delete(self, todo_id):
        todo = TodoService.get_todo(todo_id)
        if not todo:
            abort(404, message="Todo not found")
        TodoService.delete_todo(todo)
        return '', 204

@api.route('/todo')
class TodoListResource(Resource):
    @api.expect(api.model('Todo', todo_model))
    @marshal_with(todo_resource_fields)
    def post(self):
        args = todo_update_args.parse_args()
        todo = TodoService.add_todo(args['title'], args['description'], args['completed'])
        return todo, 201
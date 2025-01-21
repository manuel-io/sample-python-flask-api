from app.domain.models.todo import TodoModel
from app.infrastructure.extensions import db

class TodoService:
    @staticmethod
    def get_todo(todo_id):
        return TodoModel.query.get(todo_id)

    @staticmethod
    def add_todo(title, description, completed):
        todo = TodoModel(title=title, description=description, completed=completed)
        db.session.add(todo)
        db.session.commit()
        return todo

    @staticmethod
    def update_todo(todo, title, description, completed):
        todo.title = title
        todo.description = description
        todo.completed = completed
        db.session.commit()
        return todo

    @staticmethod
    def delete_todo(todo):
        db.session.delete(todo)
        db.session.commit()
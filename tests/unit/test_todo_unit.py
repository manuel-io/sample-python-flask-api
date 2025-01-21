import unittest

from app.domain.models.todo import TodoModel

class TodoUnitTestCase(unittest.TestCase):
    def test_todo_model(self):
        todo = TodoModel(title="Test Todo", description="Test Description", completed=False)
        self.assertEqual(todo.title, "Test Todo")
        self.assertEqual(todo.description, "Test Description")
        self.assertFalse(todo.completed)

if __name__ == '__main__':
    unittest.main()
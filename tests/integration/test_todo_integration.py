import unittest
from app import create_app
from app.domain.models.todo import TodoModel
from app.infrastructure.extensions import db

class TodoIntegrationTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_todo(self):
        with self.app.app_context():
            todo = TodoModel(id=1, title="Test Todo", description="Test Description", completed=False)
            db.session.add(todo)
            db.session.commit()

        response = self.client.get('/api/todo/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test Todo', response.get_data(as_text=True))

    def test_put_todo(self):
        response = self.client.put('/api/todo/1', json={
            'title': 'New Todo',
            'description': 'New Description',
            'completed': False
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('New Todo', response.get_data(as_text=True))

    def test_patch_todo(self):
        with self.app.app_context():
            todo = TodoModel(id=1, title="Test Todo", description="Test Description", completed=False)
            db.session.add(todo)
            db.session.commit()

        response = self.client.patch('/api/todo/1', json={
            'title': 'Updated Todo'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Updated Todo', response.get_data(as_text=True))

    def test_delete_todo(self):
        with self.app.app_context():
            todo = TodoModel(id=1, title="Test Todo", description="Test Description", completed=False)
            db.session.add(todo)
            db.session.commit()

        response = self.client.delete('/api/todo/1')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
import unittest
from app import app, db, User, Task

class TaskManagerTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_registration(self):
        rv = self.app.post('/register', data=dict(username="u1", email="u1@t.com", password="1"), follow_redirects=True)
        self.assertEqual(rv.status_code, 200)

    def test_login(self):
        self.app.post('/register', data=dict(username="u1", email="u1@t.com", password="1"))
        rv = self.app.post('/login', data=dict(email="u1@t.com", password="1"), follow_redirects=True)
        self.assertIn(b'Dashboard', rv.data)

    def test_admin_assignment(self):
        self.app.post('/register', data=dict(username="admin", email="a@t.com", password="1"))
        user = User.query.first()
        self.assertEqual(user.role, 'Admin')

    def test_task_creation(self):
        self.app.post('/register', data=dict(username="admin", email="a@t.com", password="1"))
        self.app.post('/login', data=dict(email="a@t.com", password="1"))
        self.app.post('/task/new', data=dict(title="Test", description="Desc", assigned_to=1), follow_redirects=True)
        self.assertEqual(Task.query.count(), 1)

    def test_unauthorized(self):
        rv = self.app.get('/dashboard', follow_redirects=True)
        self.assertIn(b'Login', rv.data)

if __name__ == '__main__':
    unittest.main()
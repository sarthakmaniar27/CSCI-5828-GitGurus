import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 302)

    def test_login_successful(self):
        response = self.app.post('/login', data=dict(
            username="test_user",
            password="test_password"
        ))
        self.assertEqual(response.status_code, 302) # expect redirect to dashboard page

    def test_login_unsuccessful(self):
        response = self.app.post('/login', data=dict(
            username="invalid_user",
            password="invalid_password"
        ))
        self.assertIn(b"Invalid credentials", response.data) # expect error message

    # def test_register_successful(self):
    #     response = self.app.post('/register', data=dict(
    #         name="Test User",
    #         email="test_user@example.com",
    #         username="test_user",
    #         password="test_password",
    #         confirm_password="test_password"
    #     ))
    #     self.assertEqual(response.status_code, 302) # expect redirect to dashboard page

    def test_register_invalid_email(self):
        response = self.app.post('/register', data=dict(
            name="Test User",
            email="invalid_email",
            username="test_user",
            password="test_password",
            confirm_password="test_password"
        ))
        self.assertIn(b"Invalid email address", response.data) # expect error message

    def test_register_invalid_username_length(self):
        response = self.app.post('/register', data=dict(
            name="Test User",
            email="test_user@example.com",
            username="short",
            password="test_password",
            confirm_password="test_password"
        ))
        self.assertIn(b"Length of username should be 8 to 12 characters", response.data) # expect error message

    def test_register_passwords_do_not_match(self):
        response = self.app.post('/register', data=dict(
            name="Test User",
            email="test_user@example.com",
            username="test_user",
            password="test_password",
            confirm_password="wrong_password"
        ))
        self.assertIn(b"Passwords do not match", response.data) # expect error message

    def test_dashboard_without_login(self):
        response = self.app.get('/dashboard')
        self.assertEqual(response.status_code, 302) # expect redirect to login page

    def test_dashboard_with_login(self):
        with self.app.session_transaction() as session:
            session['username'] = 'test_user'
        response = self.app.get('/dashboard')
        self.assertEqual(response.status_code, 200) # expect successful page load

    def test_logout(self):
        with self.app.session_transaction() as session:
            session['username'] = 'test_user'
        response = self.app.get('/logout')
        with self.app.session_transaction() as session:
            self.assertNotIn('username', session) # expect session to be cleared
        self.assertEqual(response.status_code, 302) # expect redirect to login page

    def test_about(self):
        response = self.app.get('/about')
        self.assertEqual(response.status_code, 200) # expect successful page load


if __name__ == '__main__':
    unittest.main()

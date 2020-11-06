import json
import bcrypt
import jwt

from django.test   import TestCase, Client
from unittest.mock import patch, MagicMock

from my_settings import SECRET, ALGORITHM
from user.models import User

client = Client()

class SignUpTest(TestCase):
    def setUp(self):
        hashed_password = bcrypt.hashpw('test1234!'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        User.objects.create(email='test@test.com', password=hashed_password)

    def tearDown(self):
        User.objects.filter(email='test@test.com').delete()

    def test_signup_success(self):
        response = client.post('/account/signup', {'email': 'test_email@test.com', 'password': 'test1234!'}, content_type = 'application/json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {"Message": "ACCOUNT_SUCCESSFULLY_CREATED"})

    def test_signup_invalid_email(self):
        response = client.post('/account/signup', {'email': 'test.com', 'password': 'test1234!'}, content_type = 'application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"Message": "INVALID_EMAIL"})

    def test_signup_ivalid_password(self):
        response = client.post('/account/signup', {'email': 'test_email2@test.com', 'password': 'test'}, content_type = 'application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"Message": "INVALID_PASSWORD"})

    def test_signup_duplicated_email(self):
        response = client.post('/account/signup', {'email': 'test@test.com', 'password': 'test1234!'}, content_type = 'application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"Message": "EMAIL_ALREADY_EXISTS"})

    def test_signup_key_error(self):
        response = client.post('/account/signup', {}, content_type = 'application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"Message": "KEY_ERROR"})


class LoginTest(TestCase):
    def setUp(self):
        hashed_password = bcrypt.hashpw('test1234!'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        User.objects.create(email='test@test.com', password=hashed_password)

    def tearDown(self):
        User.objects.get(email='test@test.com').delete()

    def test_login_success(self):
        response = client.post('/account/login', {'email': 'test@test.com', 'password': 'test1234!'}, content_type = 'application/json')

        self.assertEqual(response.status_code, 200)

    def test_login_fail(self):
        response = client.post('/account/login', {'email': 'wrongemail@test.com', 'password': 'test'}, content_type = 'application/json')

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {"Message": "INCORRECT_EMAIL_OR_PASSWORD"})

    def test_login_key_error(self):
        response = client.post('/account/login', {}, content_type = 'application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"Message": "KEY_ERROR"})

class kakaoLoginTest(TestCase):
    def setUp(self):
        User.objects.create(social_login_id=1234)

    def tearDown(self):
        User.objects.get(social_login_id=1234).delete()

    @patch('user.views.requests')
    def test_kakaologin_success(self, mocked_request):

        class KakaoResponse:
            def json(self):
                return {
                    "id": 1234
                }

        mocked_request.get = MagicMock(return_value = KakaoResponse())

        header             = {"HTTP_Authorization": "kakao_token"}
        response           = client.get('/account/login/kakao', content_type = 'application/json', **header)

        self.assertEqual(response.status_code, 200)

    @patch('user.views.requests')
    def test_kakaologin_fail(self, mocked_request):

        class KakaoResponse:
            def json(self):
                return {
                    "Message": "INVALID_TOKEN"
                }

        mocked_request.get = MagicMock(return_value = KakaoResponse())
        header             = {"HTTP_Authorization": "kakao_token"}
        response           = client.get('/account/login/kakao', content_type = 'application/json', **header)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {"Message": "INVALID_TOKEN"})


if __name__ == '__main__':
    unittest.main()

import json
import re
import bcrypt
import jwt
import requests
import urllib3

from django.http  import JsonResponse
from django.views import View

from my_settings import SECRET, ALGORITHM
from user.models import User

class SignUpView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            email    = data['email']
            password = data['password']

            email_pattern    = '^[\w\.]+@([\w]+\.)+[\w]{2,4}$'
            password_pattern = '^(?=.*[\d])(?=.*[!@#$%^&*\-])(?=.*[A-Za-z])[\w\-\.!@#$%^&*]{8,}$'

            if not re.match(email_pattern, email):
                 return JsonResponse({"Message": "INVALID_EMAIL"}, status=400)

            if not re.search(password_pattern, password):
                return JsonResponse({"Message": "INVALID_PASSWORD"}, status=400)

            if User.objects.filter(email=email).exists():
                return JsonResponse({"Message": "EMAIL_ALREADY_EXISTS"}, status=400)

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            User.objects.create(
                email    = email,
                password = hashed_password
            )
            return JsonResponse({"Message": "ACCOUNT_SUCCESSFULLY_CREATED"}, status=201)

        except KeyError:
            return JsonResponse({"Message": "KEY_ERROR"}, status=400)

class LoginView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            email    = data['email']
            password = data['password']

            user          = User.objects.get(email=email)
            user_password = user.password.encode('utf-8')

            if bcrypt.checkpw(password.encode('utf-8'), user_password):
                access_token = jwt.encode({'user_id': user.id}, SECRET['secret'], ALGORITHM['algorithm']).decode('utf-8')

                return JsonResponse({"Authorization": access_token}, status=200)

            else:
                return JsonResponse({"Message": "INCORRECT_EMAIL_OR_PASSWORD"}, status=401)

        except User.DoesNotExist:
            return JsonResponse({"Message": "INCORRECT_EMAIL_OR_PASSWORD"}, status=401)

        except KeyError:
            return JsonResponse({"Message": "KEY_ERROR"}, status=400)

class KakaoLoginView(View):
    def get(self, request):
        urllib3.disable_warnings()
        access_token = request.headers['Authorization']
        headers      = {"Authorization": f"Bearer {access_token}"}
        url          = "https://kapi.kakao.com/v2/user/me"
        response     = requests.get(url, headers=headers, verify=False)
        user         = response.json()

        if user.get('id'):
            user         = User.objects.get_or_create(social_login_id=user.get('id'))[0]
            access_token = jwt.encode({'id': user.id}, SECRET['secret'], ALGORITHM['algorithm']).decode('utf-8')

            return JsonResponse({"Authorization": access_token}, status=200)

        return JsonResponse({"Message": "INVALID_TOKEN"}, status=401)

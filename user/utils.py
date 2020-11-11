import json
import jwt
import requests

from django.http import JsonResponse

from .models     import User
from my_settings import SECRET, ALGORITHM

def login_required(f):
    def wrapper(self, request, *args, **kwargs):

        if "Authorization" not in request.headers:
            return JsonResponse({"Message": "TOKEN_DOES_NOT_EXIST"}, status=401)

        access_token = request.headers["Authorization"]

        try:
            data = jwt.decode(access_token, SECRET['secret'], ALGORITHM['algorithm'])
            user = User.objects.get(id=data['user_id'])
            request.user = user

        except jwt.DecodeError:
            return JsonResponse({"Error_code": "INVALID TOKEN"}, status=401)

        except User.DoesNotExists:
            return JsonResponse({"Error_code": "UNKNOWN USER"}, status=401)

        return f(self, request, *args, **kwargs)

    return wrapper


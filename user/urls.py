from django.urls import path
from .views      import SignUpView, LoginView, KakaoLoginView

urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/login', LoginView.as_view()),
    path('/login/kakao', KakaoLoginView.as_view()),
]

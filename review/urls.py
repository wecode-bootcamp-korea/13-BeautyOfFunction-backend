from django.urls import path
from .views import ReviewView

urlpatterns = [
    path('/get', ReviewView.as_view())
]

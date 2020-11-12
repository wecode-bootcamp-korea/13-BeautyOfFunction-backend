from django.urls import path
from .views      import (
    HairProfileView,
    HairGoalView,
    CustomizingView,
    ProductOptionView
)

urlpatterns = [
    path('/hair-profile', HairProfileView.as_view()),
    path('/hair-goals', HairGoalView.as_view()),
    path('/appearance-and-fragrance', CustomizingView.as_view()),
    path('/size-and-frequency', ProductOptionView.as_view()),
]

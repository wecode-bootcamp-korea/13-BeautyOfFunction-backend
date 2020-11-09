from django.urls import path
from .views import CategoriesView, CategoryView


urlpatterns = [
    path('',CategoriesView.as_view()),
    path('/<int:category_id>',CategoryView.as_view())
]

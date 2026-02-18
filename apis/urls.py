# apis/urls.py
from django.urls import path

from .views import ListTodo, DetaiTodo

urlpatterns = [
    path("", ListTodo.as_view()),
    path("<int:pk>/", DetaiTodo.as_view()),
]
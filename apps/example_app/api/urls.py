from django.urls import path

from apps.example_app.api import views

urlpatterns = [
    path('hello/', views.hello_view, name='hello_view'),
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.check_password, name="check_password"),
]
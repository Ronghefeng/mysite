from django.urls import path

from . import views

app_name = "login"
urlpatterns = [
    path("", views.login, name="index"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout, name="logout"),
    path("detail/", views.index, name="detail"),
]

from django.urls import path
from .views import home, password_change, register
urlpatterns = [
    path("", home, name="home"),
    path("register", register, name="register"),
    path("password-change",password_change, name="password-change" )
]
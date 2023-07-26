from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='index'),  # Change the URL pattern to an empty string
    path("home", views.Home, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("signup", views.signup, name='signup'),
    path("signin", views.signin, name='signin'),
    path("logout", views.Logout, name='logout'),
    path("post", views.create_post, name='post'),
]

# This file wasn't automatically created by django, in fact
# we created it and we're gonna define urlpatterns just like
# before. Also recall that we have to include this in our
# main urls.py

from django.urls import path
# from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),

    
    path("", views.profiles, name='profiles'),
    path("profile/<str:pk>/", views.userProfile, name="user-profile")
]
from django.urls import path
from . import views

urlpatterns = [  # beware of the naming, it should be as it is or will throw error
    path('', views.projects, name="projects"),
    path('project/<str:pk>/', views.project, name="project"),
]

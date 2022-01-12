from django.urls import path
from . import views

urlpatterns = [  # beware of the naming, it should be as it is or will throw error
    path('', views.projects, name="projects"),
    path('project/<str:pk>/', views.project, name="project"),

    # CRUD without R(Read is above) path
    path('create-project/', views.createProject, name="create-project"),

    path('update-project/<str:pk>/', views.updateProject, name='update-project'),

    path('delete-project/<str:pk>/', views.deleteProject, name='delete-project'),
]

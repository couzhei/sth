"""sth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# from django.http import HttpResponse

# # writing these functions here is so impractical and nonstandard!
# def projects(request):
#     return HttpResponse('Here are our products')

# def project(request, pk):
#     return HttpResponse(f'This is the project with id {pk}.')

from django.urls import include

# we need to add in a few things in this file(roor's urls.py) here
# so basically we just need to add a path to actually find those
# images

from django.conf import settings  # because we want to connect to our media root

# and our media url(MEDIA_URL and MEDIA_ROOT)
from django.conf.urls.static import static

# static is basically going to help us create a new URL for our static
# files

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('projects/', projects, name="projects"),
    # path('project/<str:pk>/', project, name="project"), # cool to know, but not very practical though, see urls.py under projects directory
    path("", include("projects.urls")), # '' means that's gonna be our root domain
]

# go ahead and set a new URL path
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# recall that MEDIA_ROOT is where we send the user uploaded content and
# we just created a file path. So Django before did not know how to 
# actually set that and we didn't have a url route for that. As you
# can see we just created that, we used the static method, we went into 
# settings, grab the URL and connected it to MEDIA_ROOT and that also
# depends on the above urlpatterns as well (????)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# django still doesn't know how to serve these up
# we're gonna need a third party package called Django White Noise
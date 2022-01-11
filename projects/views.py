from django.shortcuts import render
# render will look into the DIR key in TEMPLATES dictionary
# in settings.py

# Create your views here.
from django.http import HttpResponse

from projects.models import Project

projectsList = [
    {
        'id': '1',
        'title': 'E-Commerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'This was a project where I built out my own portfolio'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'Awesome open source project I am still working on.'
    }
]

# writing these functions here is so impractical and nonstandard!


def projects(request):
    # # return HttpResponse('Here are our products')
    # page = 'projects'
    # number = 10
    # context = {
    #     'page':page,
    #     'number':number,
    #     'projects':projectsList
    # }
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html',
                  context,  # these are passed variables to jinja in html! REVOLUTIONARY!
                  )


def project(request, pk):
    # # # return HttpResponse(f'This is the project with id {pk}.')
    # # projectObj = None
    # # for i in projectsList:
    # #     if i['id'] == pk:
    # #         projectObj = i
    # projectObj = Project.objects.get(id=pk)
    # tags = projectObj.tags.all()
    # return render(request, 'projects/single-project.html',
    #               {'project': projectObj,
    #               'tags':tags})
    # The following works the same as above but instead we're gonna
    # render the query right in the html page, check single-project.html
    projectObj = Project.objects.get(id=pk)
    return render(request, 'projects/single-project.html',
                  {'project': projectObj})

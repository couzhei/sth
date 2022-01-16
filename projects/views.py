from django.shortcuts import render

# render will look into the DIR key in TEMPLATES dictionary
# in settings.py

# Create your views here.
from django.http import HttpResponse

from projects.models import Project

# To use our form
from .forms import ProjectForm
from django.shortcuts import redirect

# To make use of redirect

# projectsList = [
#     {
#         'id': '1',
#         'title': 'E-Commerce Website',
#         'description': 'Fully functional ecommerce website'
#     },
#     {
#         'id': '2',
#         'title': 'Portfolio Website',
#         'description': 'This was a project where I built out my own portfolio'
#     },
#     {
#         'id': '3',
#         'title': 'Social Network',
#         'description': 'Awesome open source project I am still working on.'
#     }
# ]

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
    context = {"projects": projects}
    return render(
        request,
        "projects/projects.html",
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
    return render(request, "projects/single-project.html", context={"project": projectObj})


# after creating each view we need to create a url path in urls.py
def createProject(request):
    form = ProjectForm()

    if request.method == "POST":
        # # First let's check the terminal to see what the fuck this req is
        # # actually doing! We can access values like request.POST['title']
        # print(request.POST)
        # form = ProjectForm(request.POST)
        form = ProjectForm(request.POST, request.FILES)  # we can now have access
        # to the files sended by POST method
        if form.is_valid():  # this is a cool thing about modelforms, django
            # will actually check that all the fields are required or correct
            form.save()  # finally this statement makes the form a permenant
            # element of our table
            return redirect("projects")

    context = {"form": form}
    return render(request, "projects/project-form.html", context)


def updateProject(request, pk):  # it's very similar to the above, with
    # a few differences and one is that we need to pass an argument
    # to indicate which data point we are going to change
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == "POST":

        # form = ProjectForm(request.POST, instance=project)

        form = ProjectForm(request.POST, request.FILES, instance=project)

        if form.is_valid():
            form.save()
            return redirect("projects")

    context = {"form": form}
    return render(request, "projects/project-form.html", context)


# creating a function-based view :/
def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method =='POST':
        project.delete()
        return redirect('projects')
        """Do not forget that csrf tag
            Forbidden (403)
            CSRF verification failed. Request aborted."""
    context = {'object': project}
    return render(request, 'projects/delete_template.html', context)

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from.models import Project, Task
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'index.html')

def hello(request, username):
    return HttpResponse(f"<h2>¡Hola, %s!</h2>" % username)

def about(request):
    return render(request, 'about.html')

def projects(request):
    projects = list(Project.objects.values())
    return render(request, 'projects.html', {'projects': projects})

def tasks(request):
    tasks = list(Task.objects.values())
    return render(request, 'tasks.html', {'tasks': tasks})
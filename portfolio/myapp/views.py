from django.shortcuts import render
from .models import Project

# home page.
def home(request):
    return render(request,"myapp/home.html")

# skill page
def skill(request):
    return render(request,"myapp/skills.html")

# projects page
def projects(request):
    projects=Project.published.all()
    return render(request,"myapp/projects.html",{'projects':projects}) 



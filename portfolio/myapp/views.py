from django.shortcuts import render
from .models import Project
from django.core.paginator import Paginator

# home page.
def home(request):
    return render(request,"myapp/home.html")

# skill page
def skill(request):
    return render(request,"myapp/skills.html")

# projects page
def projects(request):
    project_list=Project.published.all()
    # pagination with 2 posts per page
    paginator=Paginator(project_list,2)
    page_number=request.GET.get('page',1)
    projects=paginator.page(page_number)
    return render(request,"myapp/projects.html",{'projects':projects}) 



from django.shortcuts import render

# home page.
def home(request):
    return render(request,"myapp/home.html")

# skill page
def skill(request):
    return render(request,"myapp/skills.html")

# projects page
def projects(request):
    return render(request,"myapp/projects.html") 



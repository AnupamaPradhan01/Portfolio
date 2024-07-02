from django.urls import path
from .import views
urlpatterns = [
    path("",views.home,name="home"),
    path("skills/",views.skill,name="skill"),
    path("projects/",views.projects,name="projects"),
]

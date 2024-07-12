from django.urls import path
from .import views


urlpatterns = [
    path("",views.home,name="home"),
    path("skills/",views.skill,name="skill"),
    path("projects/",views.projects,name="projects"),
    path('download_cv/<int:file_id>/',views.download_cv,name='download_cv'),
    path('contact/',views.Contactus,name='contact'),
    path('success/', views.success, name='success'),
]

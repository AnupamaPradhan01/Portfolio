from django.urls import path
from .import views


urlpatterns = [
    path("",views.home,name="home"),
    path("skills/",views.skill,name="skill"),
    path("projects/",views.projects,name="projects"),
    path("<int:id>/",views.detail,name="detail"),
    path('download-cv/',views.download_cv,name='download_cv'),
    path('contact/',views.Contactus,name='contact'),
    path('success/', views.success, name='success'),
    path('<int:project_id>/comment/',views.comment,name='comment'),
]

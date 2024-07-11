from django.shortcuts import render
from django.http import HttpResponse,FileResponse,Http404
from django.conf import settings
from .models import Project,UploadedFile
from django.core.paginator import Paginator
import os


# home page.
def home(request):
    files=UploadedFile.objects.all()
    return render(request,"myapp/home.html",{'files':files})
     

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
 

def download_cv(request,file_id):
    try:
        uploadedFile = UploadedFile.objects.get(pk=file_id)
        with open(uploadedFile.file.path, 'rb') as pdf:
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline;filename=some_file.pdf'
            return response
    except FileNotFoundError:
        raise Http404()
    
#Contact page
def Contact(request):
    return render(request,"myapp/contact.html",{'contact':Contact}) 
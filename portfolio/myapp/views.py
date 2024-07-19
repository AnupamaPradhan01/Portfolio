from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,FileResponse,Http404
from django.conf import settings
from .models import Project,UploadedFile,Comment
from django.core.paginator import Paginator
from django.core.mail import send_mail,BadHeaderError
from .forms import ContactForm,CommentForm
from django.views.decorators.http import require_POST
from django.contrib import messages
import os


# home page.
def home(request):
    files=UploadedFile.objects.all()
    # context={'home':'active'}
    return render(request,"myapp/home.html",{'files':files,'home':'active'})
     

# skill page
def skill(request):
    context={'skill':'active'}
    return render(request,"myapp/skills.html",context)

# projects page
def projects(request):
    project_list=Project.published.all()
    # pagination with 2 posts per page
    paginator=Paginator(project_list,2)
    page_number=request.GET.get('page',1)
    projects=paginator.page(page_number)
    return render(request,"myapp/projects.html",{'projects':projects,'proj':'active'}) 

# project detail page
def detail(request,id):
    project=get_object_or_404(Project,id=id,status=Project.Status.PUBLISHED)
    # list of active comments for this project
    comments=project.comments.filter(active=True)
    # form for users to comment
    form=CommentForm()
    return render(request,"myapp/detail.html",{'project':project,'comments':comments,'form':form})
 

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
def Contactus(request):
    if request.method=='POST':
        form=ContactForm(request.POST) 
        if form.is_valid():
            form.save()
            name=form.cleaned_data['name']   
            email=form.cleaned_data['y_email']
            subject=form.cleaned_data['y_subject']
            message=form.cleaned_data['y_message']
            recipients = [settings.EMAIL_HOST_USER]  # Your email where you want to receive messages
            try:
                send_mail(f'Message from {name} ({email})', message, email, recipients)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            # return redirect('success')
            messages.success(request,"Hurray!!! Message Sent.")
            return redirect('/contact/')
        messages.error(request,"Sorry!! Message not sent")  
    else:
        form=ContactForm()    
    return render(request,"myapp/contact.html",{'form':form,'contact':'active'}) 

def success(request):
    return HttpResponse('Success! Thank you for your message.')


# Comment views
@require_POST
def comment(request,project_id):
    project=get_object_or_404(Project,id=project_id,status=Project.Status.PUBLISHED)
    comment=None
    # A comment was posted
    form=CommentForm(data=request.POST)
    if form.is_valid():
        # creates a comment object without saving it to the database
        comment=form.save(commit=False)
        # assign the post to the comment
        comment.project=project
        # Save the comment to the database
        comment.save()
    return render(request,'myapp/comment.html',{'project':project,'form':form,'comment':comment})    
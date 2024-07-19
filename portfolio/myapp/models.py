from typing import Any
from django.db import models
from django.utils import timezone
# custom manager
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
                       .filter(status=Project.Status.PUBLISHED)
# projects model.

class Project(models.Model):
    class Status(models.TextChoices):
        DRAFT='DF','Draft'
        PUBLISHED='PB','Published'
    title=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200)
    body=models.TextField()
    git_link=models.CharField(max_length=200,default="fghyj")
    netlify_link=models.CharField(max_length=1000,default="iklo")
    publish=models.DateTimeField(default=timezone.now)
    status=models.CharField(max_length=2,choices=Status.choices,default=Status.DRAFT)
    
    # default manager
    objects=models.Manager()
    # custom manager
    published=PublishedManager()
    
    class Meta:
        ordering=['-publish']
        indexes=[models.Index(fields=['-publish']),]
    
    def __str__(self):
        return self.title   
    
#upload file 
class UploadedFile(models.Model):
    title=models.CharField(max_length=200,default="cv")
    file=models.FileField(upload_to='uploads/')
    uploaded_at=models.DateTimeField(auto_now_add=True)  
    
#contact me
class contact(models.Model):
    name=models.CharField(max_length=240)
    y_email=models.EmailField(max_length=250) 
    y_subject=models.CharField(max_length=200)
    y_message=models.CharField(max_length=500)
    
    def __str__(self):
        return self.name
    
#project comment
class Comment(models.Model):
    project=models.ForeignKey(Project,on_delete=models.CASCADE,related_name='comments')
    name=models.CharField(max_length=80)
    email=models.EmailField()
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    
    class Meta:
        ordering=['created']
        indexes=[
            models.Index(fields=['created']),
            
        ] 
    def __str__(self):
        return f'Comment by {self.name} on {self.project}'    
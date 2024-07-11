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
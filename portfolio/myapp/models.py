from django.db import models
from django.utils import timezone
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
    
    class Meta:
        ordering=['-publish']
        indexes=[models.Index(fields=['-publish']),]
    
    def __str__(self):
        return self.title    
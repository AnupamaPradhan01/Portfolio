from django.contrib import admin
from .models import Project,UploadedFile

# project model.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display=['title','slug','publish','status']
    date_hierarchy='publish'
    prepopulated_fields={'slug':('title',)}

@admin.register(UploadedFile)
class uploadedAdmin(admin.ModelAdmin):
    list_display=['uploaded_at']
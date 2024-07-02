from django.contrib import admin
from .models import Project

# project model.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display=['title','slug','publish','status']
    date_hierarchy='publish'
    prepopulated_fields={'slug':('title',)}

from django.contrib import admin

# Register your models here.

from .models import project, skill, tag

admin.site.register(project)
admin.site.register(skill)
admin.site.register(tag)


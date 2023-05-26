from django.db import models
import uuid
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class project(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(null = True, blank  = True)
    body = RichTextUploadingField()
    slug = models.SlugField(null = True, blank = True)
    created = models.DateTimeField(auto_now_add= True)
    id = models.UUIDField(default = uuid.uuid4,
                          unique = True,
                          primary_key  = True,
                          editable = False)

    def __str__(self):
        return self.title
    
class skill(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(blank = True)
    created = models.DateTimeField(auto_now_add= True)
    id = models.UUIDField(default = uuid.uuid4,
                          unique = True,
                          primary_key  = True,
                          editable = False)
    
    def __str__(self):
        return self.title
    
class tag(models.Model):
    name = models.CharField(max_length=200)
    
    created = models.DateTimeField(auto_now_add= True)
    id = models.UUIDField(default = uuid.uuid4,
                          unique = True,
                          primary_key  = True,
                          editable = False)
    
    def __str__(self):
        return self.name
 
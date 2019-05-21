from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils.text import slugify

def generate_slug(s):
    return slugify(s) + "-" + str(uuid.uuid4())

class UploadedFileModel(models.Model):
    slug = models.SlugField(max_length=50, unique=True)
    file = models.FileField(upload_to="uploads/")
    size = models.IntegerField()
    upload_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    deadline = models.DateTimeField(auto_now=False, auto_now_add=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        filename = self.file.name
        return filename[filename.rfind('/')+1:]
    
    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)
        

from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils.text import slugify

def generate_slug(s):
    return slugify(s) + "-" + str(uuid.uuid4())

def user_directory_path(instance, filename):
    return 'uploads/{0}/{1}'.format(instance.user.username, filename)

class UploadedFileModel(models.Model):
    slug = models.SlugField(max_length=50, unique=True)    
    size = models.IntegerField()
    upload_time = models.DateField(auto_now=False, auto_now_add=True)
    deadline = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    file = models.FileField(upload_to=user_directory_path)

    def __str__(self):
        filename = self.file.name
        return filename[filename.rfind('/')+1:]
    
    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)


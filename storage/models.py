from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils.text import slugify

def generate_slug(s):
    """
    Generates unique slug for each uploaded file. 

    s (str): Filename
    """
    return slugify(s[:10 if len(s) > 10 else -1]) + "-" + str(uuid.uuid4())

def user_directory_path(instance, filename):
    """
    Obtain the upload path, including the filename. File will be uploaded to 
    settings.MEDIA_ROOT/<username>/<filename> if user is authenticated, and
    to settings.MEDIA_ROOT/anon_usr/<filename> otherwise.

    instance: An instance of the model where the FileField is defined
    filename (str): Filename
    """

    folder = instance.user.username if instance.user else 'anon_usr'
    return 'uploads/{0}/{1}'.format(folder, filename)

class UploadedFileModel(models.Model):
    """
    Stores a single file entry, related to 'auth.User' model
    """
    slug = models.SlugField(max_length=50, unique=True)    
    size = models.IntegerField()
    upload_time = models.DateField(auto_now=False, auto_now_add=True)
    deadline = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    file = models.FileField(upload_to=user_directory_path)

    def __str__(self):
        # returns name of file like "file.ext"
        
        filename = self.file.name
        return filename[filename.rfind('/')+1:]
    
    def delete(self, *args, **kwargs):
        """
        Overriding delete method. When instance of file model will be deleted 
        from database, file deletes from server too.
        """
        self.file.delete()
        super().delete(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("storage:file_info", kwargs={"slug": self.slug})
    

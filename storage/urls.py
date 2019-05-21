from django.urls import path
from .views import *

app_name = 'storage'

urlpatterns = [
    path('', UploadFileView.as_view(), name='upload'),
    path('accounts/register', register, name='register'),
    path('<str:slug>/delete', DeleteFileView.as_view(), name='delete_file')
    # path('<str:file_id>', ),
]
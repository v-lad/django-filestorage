from django.urls import path
from .views import *

app_name = 'storage'

urlpatterns = [
    path('', UploadFileView.as_view(), name='upload'),
    path('<str:slug>/delete', DeleteFileView.as_view(), name='delete_file'),
    path('<str:slug>/', UploadedFileDetailView.as_view(), name='file_info'),
]
from django.shortcuts import render, redirect
from django.views import View
from .forms import UploadForm
from .models import UploadedFileModel, generate_slug

import datetime
import json
import base64
from django.core.files.base import ContentFile

from pprint import pprint

class UploadFileView(View):
    """
    Display upload files page with upload form 'UploadForm' and
    uploaded files, if user is authenticated. If user isn`t 
    authenticated, he will be redirected at uploaded file detail
    page as form will have submitted (unauthorized users can 
    upload only one file at a time). 
    """

    def get(self, request):
        form = UploadForm()
        context = {
            'form': form,
        }
        return render(request, 'storage/upload_file_page.html', context=context)

    def post(self, request):
        form = UploadForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = request.user
            dl = data['time']
            uploads = request.POST.getlist('upload')
            
            # Handling uploaded files (decoding from Base64 and storing to db)
            for file in uploads:
                file = json.loads(file)
                name = file['name']
                file_data = ContentFile(base64.b64decode(file['data']), name=name)

                instance = UploadedFileModel(
                    slug=generate_slug(name[:name.rfind('.')]),
                    file=file_data,
                    size=file['size'],
                    deadline=dl,
                )

                if user.is_authenticated:
                    instance.user = user

                instance.save()
            
            # If user is authenticated redirecting back to upload files page
            if user.is_authenticated:
                return redirect('/')

            # Otherwise, it`ll redirect to uploaded file detail page
            return redirect(instance)
        
        else:
            return render(request, 'storage/upload_file_page.html', context={'form': form})


class UploadedFileDetailView(View):
    """
    Display an individual file info

    Context:
      file: UploadedFileModel instance
      deletes_at: file deleting date
      days_until_delete: count of days left
    """

    def get(self, request, slug):
        file = UploadedFileModel.objects.get(slug=slug)
        upload_date = file.upload_time
        dl = file.deadline

        deletes_at = upload_date + datetime.timedelta(days=dl)
        days_until_delete = deletes_at - datetime.date.today()

        context = {
            "file": file,
            "deletes_at": deletes_at,
            "days_until_delete": days_until_delete.days,
        }

        return render(request, 'storage/file_info_page.html', context=context)


class DeleteFileView(View):
    """
    Delete file through POST request
    """

    def post(self, request, slug):
        file = UploadedFileModel.objects.get(slug=slug)
        file.delete()

        return redirect("/")

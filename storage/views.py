from django.shortcuts import render, redirect, reverse
from django.views import View
from storage.forms import UploadForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UploadForm
from .models import UploadedFileModel, generate_slug

import datetime
import json
import base64
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile

from pprint import pprint

class UploadFileView(View):
    def get(self, request):
        form = UploadForm()
        context = {
            'form': form,
        }
        return render(request, 'storage/upload_file_page.html', context=context)

    def post(self, request):
        # print()
        # pprint(request.POST)
        # print()

        form = UploadForm(request.POST)
        
        # pprint(form.errors)
        if form.is_valid():
            data = form.cleaned_data
            user = request.user
            dl = data['time']
            uploads = request.POST.getlist('upload')
            
            for file in uploads:
                file = json.loads(file)
                name = file['name']
                file_data = ContentFile(base64.b64decode(file['data']), name=name)

                instance = UploadedFileModel(
                    slug=generate_slug(name[:name.rfind('.')]),
                    file=file_data,
                    size=file['size'],
                    deadline=dl,
                    user=user
                )

                instance.save()

            # pprint(form.cleaned_data)
            # print()
            return redirect('/')
        
        else:
            return render(request, 'storage/upload_file_page.html', context={'form': form})

class UploadedFileDetailView(View):
    pass

class DeleteFileView(View):
    def post(self, request, slug):
        file = UploadedFileModel.objects.get(slug=slug)
        file.delete()
        print()
        pprint(request.POST)
        print()
        pprint(request.body)
        print()

        return redirect("/")

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        c_password = request.POST['c_password']

        # Check passwords matching
        if password != c_password:
            messages.error(request, "Passwords don`t match.")
            return redirect('/accounts/register')
        else:
            if User.objects.filter(username=username).exists(): 
                messages.error(request, "Someone have already taken that username.")
                return redirect('/accounts/register')
            else:
                if User.objects.filter(email=email).exists(): 
                    messages.error(request, "That email is being used.")
                    return redirect('/accounts/register')
                else:
                    user = User.objects.create_user(
                        username=username,
                        email=email,
                        password=password,
                    )

                    user.save()
                    messages.success(request, f"User \"{username}\" has created. You can login now")
                    return redirect('login')
        
    else:
        return render(request, 'registration/register.html')
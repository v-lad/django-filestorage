from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        c_password = request.POST['c_password']

        # Check passwords matching
        if password != c_password:
            messages.error(request, "Passwords don`t match.")
            return redirect('register')
        else:
            if User.objects.filter(username=username).exists(): 
                messages.error(request, "Someone have already taken that username.")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists(): 
                    messages.error(request, "That email is being used.")
                    return redirect('register')
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
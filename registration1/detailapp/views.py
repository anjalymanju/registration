from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"User is Invalid")
            return redirect('login')

    return render(request,"login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Exist")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Exist")
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, password=password, first_name=firstname,
                                                last_name=lastname, email=email)
                user.save()
                return redirect('login')

            print("User Created")



        else:
            messages.info(request, "Password Not Match")
            return redirect('register')
        return redirect('/')

    return render(request, "register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
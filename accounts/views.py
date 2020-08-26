from Travello.models import Destination
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponse


# Create your views here.


def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')

    else:
        return render(request,'login.html')

def register(request):

    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email taken')
                return redirect('register.html')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('register.html')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save();
                messages.info(request,'User Created')
                return redirect('login')
        else:
            messages.info(request,'password not matching...')
            return redirect('register.html')
        return redirect('/')

    else:
        return render(request,'register.html')

def home(request):
    if request.method == 'POST':
        return redirect('/')
    

def logout(request):
    auth.logout(request)
    return redirect("/")

def destinations(request, id):
    dests = Destination.objects.filter(id=id)
    return render(request, 'destinations.html', {'dests': dests})
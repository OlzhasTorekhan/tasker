from cmath import log
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import User
# Create your views here.
user_page = '/user'
def main_view(request):
    return render(request,'index.html')

def login_view(request):
    method = request.method
    match method:
        #Check methods 
        case 'GET':
            return render(request,'login.html')
        case 'POST':
            user = authenticate(request,request.POST['username'],method.POST['password'])
            if user is not None:
                #Log in the user in session
                login(request,user)
                return redirect(user_page)
            else:
                return render(request,'login.html',context={'error':1})

def logout_view(request):
    logout(request)
    return redirect('/')

def register(request):
    if request.user is not None:
        return redirect(user_page)
    match request.method:
        case 'POST':
            POST = request.POST
            user = User.objects.create(
                username=POST['username'],
                password=POST['password'],
                email=POST['email'],
                first_name=POST['first_name']
            )
            login(request,user)
            return redirect(user_page)
        case 'GET':
            return render(request,'register.html')
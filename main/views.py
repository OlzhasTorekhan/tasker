from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
# Create your views here.
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
                return redirect('/user')
            else:
                return render(request,'login.html',context={'error':1})

def logout_view(request):
    logout(request)
    return redirect('/')
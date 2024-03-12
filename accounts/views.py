from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import redirect
from django.db import IntegrityError
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreateForm




def signup_account_view(request):
    if request.method == 'GET':
        return render(request, 'accounts/signupAccount.html',{'form':UserCreateForm})
    else:
        if request.POST['password1'] == request.POST['password2']: 
            try:
                user = User.objects.create_user( request.POST['username'],password= request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('')
            except IntegrityError:
                return render(request,'accounts/signupAccount.html',{'form':UserCreateForm,'error':'Usuario ya existente, escoge otro.'})
        else:
            return render(request, 'accounts/signupAccount.html',{'form':UserCreateForm,'error':'Claves no coinciden'})

def logout_account_view(request):
    logout(request)
    return redirect('')

def login_account_view(request):
    if request.method == 'GET':
        return render(request, 'accounts/loginAccount.html',{'form':AuthenticationForm})
    else:
        user = authenticate(request,
        username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'accounts/loginAccount.html',{'form': AuthenticationForm,'error': 'Usuario y contraseña no coinciden'})
        else:
            login(request,user)
            return redirect('')
            
from audioop import add
from django.forms import EmailInput
from django.shortcuts import redirect, render 
from .models import SignUp
from .forms import  CreatUser, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages




def subscribe(request):
  if request.method == 'POST':
        email = request.POST['email']
        email = SignUp(email=email)
        signup = SignUp.objects.all()
        print(signup)
        for email_item in signup:
            print('this is the email %s :' %email)
            print('this is the email_item  %s :' %email_item)
            
            if '@' in str(email):
                email_item = str(email_item)
                email_item = email_item.strip()
                new_email = str(email)
                new_email = new_email.strip()
                if new_email == email_item:
                    print('email already exists')
                else:
                    email.save()
            else:
                print('INVALID EMAIL')
                
                
        
        
        else:
            print('not subscrbed')
        return redirect('blogview')


def register_user(request):
    form = CreatUser(request.POST or None)
    if request.method == 'POST':
        form = CreatUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogview')
        else:
            messages.info(request, 'invalid input please try again')
    context={'form':form}
    return render(request, 'account/register_user.html', context)

def login_user(request):
    form = LoginForm(request.POST)
    if request.method == 'POST':
        form = LoginForm(request.POST)
    # if i remove the print(form ) line of code bellow the function will stop working
    # i will no longer be able to login. i don't know why for now.
        print(form)
        user = authenticate(request, username=form.instance.username, password = form.instance.password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully loged in')
            
            return redirect('blogview')
        else:
            messages.info(request, 'user not found ')
    
    context = {'form':form}
    return render(request, 'account/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('blogview')
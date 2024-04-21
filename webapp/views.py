from django.shortcuts import render, redirect
from .forms import NewUser, LoginForm

# django function for logout
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate


# Create your views here.
def test_view(request):
    return render(request, 'webapp/index.html')
def base_view(request):
    return render(request, 'webapp/base.html')

#Register
def register_view(request):
    form = NewUser()
    if request.method == "POST":
        form = NewUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    resp = {'form':form}
    return render(request, 'webapp/register.html', context = resp)


# Login
def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid:
            username = request.POST.get('username') #try replacing request.POST with
            password = request.POST.get('password') #data.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                redirect('dashboard')
    context = {'form':form}
    return render(request, 'webapp/login.html', context=context)


# logout
def logout_view(request):
    auth.logout(request)
    return redirect('login')


# dashboard
def dashboard_view(request):
    return render(request, 'webapp/dashboard.html')

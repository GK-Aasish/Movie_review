from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User

# Create your views here.
def home_view(request):
    return render(request,"main/index.html")

def register_view(request):
    if request.method == "POST":
        errors = {}
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not username:
            errors['username']="Enter Username"
        if not email:
            errors['email']="Enter Email"
        if not password:
            errors['password']="Enter Password"
        if password != confirm_password:
            errors['confirm_password']="Passwords didn't match!"
        if errors:
            return render(request,"auth/register.html",{"errors":errors,"data":request.POST})

        if not errors:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            return redirect("login")
    return render(request,"auth/register.html")

def login_view(request):
    if request.method == "POST":
        errors = {}
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username:
            errors['username'] = "Enter Your Username"
        if not password:
            errors['password'] = "Enter Your Password"

        if errors:
            return render(request,"auth/login.html",{"errors":errors,"data":request.POST})

        if not errors:
            user = authenticate(request, username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
    return render(request,"auth/login.html")
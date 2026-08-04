from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,"main/index.html")

def register_view(request):
    return render(request,"auth/register.html")
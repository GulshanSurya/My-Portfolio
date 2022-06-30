from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'home.html')

def myprojects(request):
    return render(request, 'myprojects.html')

def internships(request):
    return render(request, 'internships.html')



def tables(request):
    return render(request, 'table.html')

def adder(request):
    return render(request, 'adder.html')

def webdev_django(request):
    return render(request, 'webdev_django.html')

def python(request):
    return render(request, 'python.html')

def aiml(request):
    return render(request, 'aiml.html')

def frontend(request):
    return render(request, 'frontend.html')

def oact(request):
    return render(request, 'oact.html')

def login(request):
    return render(request, 'login.html')



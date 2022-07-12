
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('myprojects/', views.myprojects, name='myprojects'),
    path('internships/', views.internships, name='internships'),
    path('oact/', views.oact, name='oact'),
    
    path('tables/', views.tables, name='tables'),
    path('adder/', views.adder, name='adder'),
    path('webdev_django/', views.webdev_django, name='webdev_django'),
    path('python/', views.python, name='python'),
    path('aiml/', views.aiml, name='aiml'),
    path('frontend/', views.frontend, name='frontend'),
    path('login/', views.login, name='login'),
    path('webdev_django/myportfoliodescribed/', views.myportfoliodescribed, name='myportfoliodescribed'),
    path('frontend/myportfoliodescribed/', views.myportfoliodescribed, name='myportfoliodescribed'),
    path('myprojects/home', views.home, name='home'),
    
    
    
]

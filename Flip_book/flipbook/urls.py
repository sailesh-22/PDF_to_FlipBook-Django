# flipbook/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('pdf2flipbook/', views.pdf2flipbook, name='pdf2flipbook'),
    path('open_flipbook/<str:file_name>/', views.open_flipbook, name='open_flipbook'),
    path('flipbooks/', views.flipbooks, name='flipbooks'),
   
    
]

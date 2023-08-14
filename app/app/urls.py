from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('userlogin/', views.userlogin, name='userlogin'),
    path('hospitallogin/', views.hospitallogin, name='hospitallogin'),
    path('usersignup/', views.usersignup, name='usersignup'),
    path('hospitalsignup/', views.hospitalsignup, name='hospitalsignup'),
    path('hospitalbedmanagement/', views.hospitalbedmanagement, name='hospitalbedmanagement'),
    path('bedstatus/', views.bedstatus, name='bedstatus'),
    path('bookbed/<str:hospitalcode>', views.bookbed, name='bookbed'),
    path('patient/', views.patient, name='patient'),
    path('logout/', views.logout, name='logout'),
    path('hlogout/', views.hlogout, name='hlogout'),
]
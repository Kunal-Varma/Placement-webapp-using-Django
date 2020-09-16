from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name= "index"),
    # Authentication
    path('register/', views.register_page, name= "register_page"),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    
    path('TPO_app/', views.register_student, name= "register_student"),
    path('register_job/', views.register_job, name= "register_job"),
    path('register_student_submit/', views.register_student_submit, name= "register_student_submit"),
    path('register_job_submit/', views.register_job_submit, name= "register_job_submit"),
    path('companies/', views.companies, name= "companies"),
    path('upcoming_events/', views.upcoming_events, name= "upcoming_events"),
    path('upcoming_events_submit/', views.upcoming_events_submit, name= "upcoming_events_submit"),
    path('add_company/', views.add_company, name= "add_company"),
    path('add_company_submit/', views.add_company_submit, name= "add_company_submit"),
    path('Statistics/', views.Statistics, name= "Statistics"),
    
    
]

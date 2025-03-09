from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('dashboard/', views.dashboard_redirect, name='dashboard'),
    path('dashboard/student/', views.student_dashboard, name='student_dashboard'),
    path('dashboard/teacher/', views.teacher_dashboard, name='teacher_dashboard'),
    path('dashboard/manager/', views.manager_dashboard, name='manager_dashboard'),
]

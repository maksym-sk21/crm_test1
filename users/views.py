from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Student, Teacher, Manager
from django.http import HttpResponse


def home(request) -> HttpResponse:
    return render(request, "index.html")


@login_required
def dashboard_redirect(request):
    """ Перенаправление в нужный кабинет в зависимости от роли пользователя """
    user = request.user
    if user.is_manager:
        return redirect('manager_dashboard')
    elif user.is_teacher:
        return redirect('teacher_dashboard')
    elif user.is_student:
        return redirect('student_dashboard')
    else:
        return redirect('home')


@login_required
def student_dashboard(request):
    student = Student.objects.get(user=request.user)
    return render(request, 'dashboard/student_dashboard.html', {'student': student})


@login_required
def teacher_dashboard(request):
    teacher = Teacher.objects.get(user=request.user)
    return render(request, 'dashboard/teacher_dashboard.html', {'teacher': teacher})


@login_required
def manager_dashboard(request):
    manager = Manager.objects.get(user=request.user)
    return render(request, 'dashboard/manager_dashboard.html', {'manager': manager})

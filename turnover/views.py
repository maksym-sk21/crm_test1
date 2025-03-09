from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Turnover, School, Salary, StudentCalculation, TeacherCalculation
from django.http import HttpResponse, JsonResponse
from django.db.models import Sum, Avg
from django.views.decorators.csrf import csrf_exempt
from schedule.models import Lesson
from schedule.forms import LessonForm
from django.template.loader import render_to_string
from .forms import TurnoverForm, StudentCalculationForm, TeacherCalculationForm


def is_manager(user):
    return user.groups.filter(name='Managers').exists()


@login_required
@csrf_exempt
@user_passes_test(is_manager)
def turnover_list(request):
    turnovers = Turnover.objects.all().order_by("id")
    form = TurnoverForm()
    return render(request, 'turnover/turnover_list.html', {'turnovers': turnovers, "form": form})


@login_required
@csrf_exempt
@user_passes_test(is_manager)
def edit_turnover(request, turnover_id):
    turnover = get_object_or_404(Turnover, id=turnover_id)
    if request.method == 'POST':
        form = TurnoverForm(request.POST, instance=turnover)
        if form.is_valid():
            form.save()
            return render(request, "turnover/turnover_item.html", {"turnover": turnover})
        else:
            return JsonResponse({"errors": form.errors}, status=400)
    else:
        form = TurnoverForm(instance=turnover)
        return render(request, "turnover/turnover_edit_form.html",{"form": form, "turnover": turnover})


@login_required
@csrf_exempt
@user_passes_test(is_manager)
def add_turnover(request):
    if request.method == "POST":
        form = TurnoverForm(request.POST)
        if form.is_valid():
            form.save()
            turnovers = Turnover.objects.all().order_by("id")
            return render(request, "turnover/turnover_list_partial.html", {"turnovers": turnovers})
    return HttpResponse(status=400)


@login_required
@csrf_exempt
@user_passes_test(is_manager)
def delete_turnover(request, turnover_id: int) -> HttpResponse:
    turnover = get_object_or_404(Turnover, id=turnover_id)
    turnover.delete()
    turnovers = Turnover.objects.all().order_by("id")
    return render(request, "turnover/turnover_list_partial.html", {"turnovers": turnovers})


@login_required
@csrf_exempt
@user_passes_test(is_manager)
def school_list(request):
    schools = School.objects.all().order_by("id")
    return render(request, 'school/school_list.html', {'schools': schools})


@login_required
@csrf_exempt
@user_passes_test(is_manager)
def salary_list(request):
    salaries = Salary.objects.all().order_by("id")
    return render(request, 'salary/salary_list.html', {'salaries': salaries})


@login_required
@csrf_exempt
@user_passes_test(is_manager)
def student_calculation_list(request):
    student_calculations = StudentCalculation.objects.all().order_by("id")
    return render(request, 'student_calculation/student_calculation_list.html',
                  {'student_calculations': student_calculations})


@login_required
@csrf_exempt
@user_passes_test(is_manager)
def edit_student_calculation(request, student_calculation_id):
    student_calculation = get_object_or_404(StudentCalculation, id=student_calculation_id)
    if request.method == 'POST':
        form = StudentCalculationForm(request.POST, instance=student_calculation)
        if form.is_valid():
            form.save()
            return render(request, "student_calculation/student_calculation_item.html",
                          {"student_calculation": student_calculation})
        return JsonResponse({"errors": form.errors}, status=400)
    else:
        form = StudentCalculationForm(instance=student_calculation)
        return render(request, "student_calculation/student_calculation_edit.html",
                      {"form": form, "student_calculation": student_calculation})


@login_required
@csrf_exempt
@user_passes_test(is_manager)
def teacher_calculation_list(request):
    teacher_calculations = TeacherCalculation.objects.all().order_by("id")
    return render(request, 'teacher_calculation/teacher_calculation_list.html',
                  {'teacher_calculations': teacher_calculations})


@login_required
@csrf_exempt
@user_passes_test(is_manager)
def edit_teacher_calculation(request, teacher_calculation_id):
    teacher_calculation = get_object_or_404(TeacherCalculation, id=teacher_calculation_id)
    if request.method == 'POST':
        form = TeacherCalculationForm(request.POST, instance=teacher_calculation)
        if form.is_valid():
            form.save()
            return render(request, "teacher_calculation/teacher_calculation_item.html",
                          {"teacher_calculation": teacher_calculation})
        return JsonResponse({"errors": form.errors}, status=400)
    else:
        form = TeacherCalculationForm(instance=teacher_calculation)
        return render(request, "teacher_calculation/teacher_calculation_edit.html",
                      {"form": form, "teacher_calculation": teacher_calculation})


@login_required
@user_passes_test(is_manager)
def manage_schedule(request):
    lessons = Lesson.objects.all().order_by('date')
    form = LessonForm()
    return render(request, 'schedule/schedule.html', {'lessons': lessons, 'form': form})


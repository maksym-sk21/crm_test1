from django.urls import path
from . import views

urlpatterns = [
    path("turnovers/", views.turnover_list, name="turnover_list"),
    path("turnovers/create/", views.add_turnover, name="add_turnover"),
    path("turnovers/edit/<int:turnover_id>/", views.edit_turnover, name="edit_turnover"),
    path("turnovers/<int:turnover_id>/delete/", views.delete_turnover, name="delete_turnover"),
    path("salaries/", views.salary_list, name="salary_list"),
    path("schools/", views.school_list, name="school_list"),
    path("student_calculations/", views.student_calculation_list, name="student_calculation_list"),
    path("student_calculations/<int:student_calculation_id>/update/", views.edit_student_calculation,
         name="edit_student_calculation"),
    path("teacher_calculations/", views.teacher_calculation_list, name="teacher_calculation_list"),
    path("teacher_calculations/<int:teacher_calculation_id>/update/", views.edit_teacher_calculation,
         name="edit_teacher_calculation"),
    path('schedule/', views.manage_schedule, name='manage_schedule'),

]

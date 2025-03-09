from django import forms
from .models import Turnover, TeacherCalculation, School, Salary, StudentCalculation
# from users.models import Student, Teacher
from django.db import transaction
from .signals import update_related_models, update_teacher_budget


class TurnoverForm(forms.ModelForm):
    # student = forms.ModelChoiceField(queryset=Student.objects.all(),
    #                                  widget=forms.Select(attrs={'class': 'form-control'}))
    # teacher = forms.ModelChoiceField(queryset=Teacher.objects.all(),
    #                                  widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Turnover
        fields = [
            'student',
            'teacher',
            'previous_hours',
            'previous_balance',
            'current_hours',
            'current_payment',
            'total_hours',
            'profit'
        ]
        widgets = {
            'previous_hours': forms.NumberInput(attrs={'class': 'form-control'}),
            'previous_balance': forms.NumberInput(attrs={'class': 'form-control'}),
            'current_hours': forms.NumberInput(attrs={'class': 'form-control'}),
            'current_payment': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_hours': forms.NumberInput(attrs={'class': 'form-control'}),
            'profit': forms.NumberInput(attrs={'class': 'form-control'}),
        }

        def save(self, commit=True):
            instance = super().save(commit=False)
            if commit:
                with transaction.atomic():
                    update_related_models(sender=Turnover, instance=instance, created=True)
                    instance.save()

            return instance


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = [
            'turnover',
            'total_profit',
            'school_budget',
            'budget_admin',
            'budget_owner'
        ]
        widgets = {
            'turnover': forms.Select(attrs={'class': 'form-control'}),
            'total_profit': forms.NumberInput(attrs={'class': 'form-control'}),
            'school_budget': forms.NumberInput(attrs={'class': 'form-control'}),
            'budget_admin': forms.NumberInput(attrs={'class': 'form-control'}),
            'budget_owner': forms.NumberInput(attrs={'class': 'form-control'})
        }


class SalaryForm(forms.ModelForm):
    class Meta:
        model = Salary
        fields = [
            'turnover',
            'monthly_profit',
            'monthly_budget',
            'salary_admin',
            'salary_owner'
        ]
        widgets = {
            'turnover': forms.Select(attrs={'class': 'form-control'}),
            'monthly_profit': forms.NumberInput(attrs={'class': 'form-control'}),
            'monthly_budget': forms.NumberInput(attrs={'class': 'form-control'}),
            'salary_admin': forms.NumberInput(attrs={'class': 'form-control'}),
            'salary_owner': forms.NumberInput(attrs={'class': 'form-control'})
        }


class StudentCalculationForm(forms.ModelForm):
    class Meta:
        model = StudentCalculation
        fields = [
            'turnover',
            'hourly_rate',
            'money_spent',
            'remaining_hours',
            'remaining_money'
        ]
        widgets = {
            'turnover': forms.Select(attrs={'class': 'form-control'}),
            'hourly_rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'money_spent': forms.NumberInput(attrs={'class': 'form-control'}),
            'remaining_hours': forms.NumberInput(attrs={'class': 'form-control'}),
            'remaining_money': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class TeacherCalculationForm(forms.ModelForm):
    class Meta:
        model = TeacherCalculation
        fields = [
            'turnover',
            'hourly_rate',
            'hours_spent',
            'salary_teacher',
            'budget_teacher'
        ]
        widgets = {
            'turnover': forms.Select(attrs={'class': 'form-control'}),
            'hourly_rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'hours_spent': forms.NumberInput(attrs={'class': 'form-control'}),
            'salary_teacher': forms.NumberInput(attrs={'class': 'form-control'}),
            'budget_teacher': forms.NumberInput(attrs={'class': 'form-control'}),
        }

        def save(self, commit=True):
            instance = super().save(commit=False)
            if commit:
                print(f"Form saved: Hourly Rate: {instance.hourly_rate}")
                with transaction.atomic():
                    update_teacher_budget(sender=TeacherCalculation, instance=instance, created=True)
            return instance

#
# class AssignStudentForm(forms.Form):
#     student = forms.ModelChoiceField(queryset=Student.objects.all(), label="Выберите студента")
#
#
# class TeacherForm(forms.ModelForm):
#     class Meta:
#         model = Teacher
#         fields = ['name', 'surname', 'phone_number']
#
#
# class StudentForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = ['name', 'surname', 'phone_number']

from django.db import models
from users.models import Student, Teacher
from django.utils import timezone
from decimal import Decimal
# Create your models here.


class Turnover(models.Model):
    date = models.DateField(default=timezone.now)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    previous_hours = models.DecimalField(max_digits=10, decimal_places=1, blank=True, default=0)
    previous_balance = models.DecimalField(max_digits=10, decimal_places=1, blank=True, default=0)
    current_hours = models.DecimalField(max_digits=10, decimal_places=1, blank=True, default=0)
    current_payment = models.DecimalField(max_digits=10, decimal_places=1, blank=True, default=0)
    total_hours = models.DecimalField(max_digits=10, decimal_places=1, blank=True, default=0)
    profit = models.DecimalField(max_digits=10, decimal_places=1, blank=True, default=0)

    def save(self, *args, **kwargs):
        self.total_hours = Decimal(self.previous_hours or 0) + Decimal(self.current_hours or 0)
        self.profit = Decimal(self.previous_balance or 0) + Decimal(self.current_payment or 0)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student.name} - {self.teacher.name}"

    class Meta:
        permissions = [
            ("can_view_turnover", "Can view turnover"),
            ("can_edit_turnover", "Can edit turnover"),
        ]


class School(models.Model):
    turnover = models.ForeignKey(Turnover, on_delete=models.CASCADE)
    total_profit = models.DecimalField(max_digits=10, decimal_places=1, null=True, default=0)
    school_budget = models.DecimalField(max_digits=10, decimal_places=1, null=True, default=0)
    budget_admin = models.DecimalField(max_digits=10, decimal_places=1, null=True, default=0)
    budget_owner = models.DecimalField(max_digits=10, decimal_places=1, null=True, default=0)

    def __str__(self):
        return f"School - {self.turnover}"

    class Meta:
        permissions = [
            ("can_view_turnover", "Can view turnover"),
            ("can_edit_turnover", "Can edit turnover"),
        ]


class Salary(models.Model):
    turnover = models.ForeignKey(Turnover, on_delete=models.CASCADE)
    monthly_profit = models.DecimalField(max_digits=10, decimal_places=1, null=True, default=0)
    monthly_budget = models.DecimalField(max_digits=10, decimal_places=1, null=True, default=0)
    salary_admin = models.DecimalField(max_digits=10, decimal_places=1, null=True, default=0)
    salary_owner = models.DecimalField(max_digits=10, decimal_places=1, null=True, default=0)

    def __str__(self):
        return f"Salary - {self.turnover}"

    class Meta:
        permissions = [
            ("can_view_turnover", "Can view turnover"),
            ("can_edit_turnover", "Can edit turnover"),
        ]


class StudentCalculation(models.Model):
    turnover = models.ForeignKey(Turnover, on_delete=models.CASCADE)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=1, null=True, default=0)
    money_spent = models.DecimalField(max_digits=10, decimal_places=1, null=True, default=0)
    remaining_hours = models.DecimalField(max_digits=10, decimal_places=1, null=True, default=0)
    remaining_money = models.DecimalField(max_digits=10, decimal_places=1, default=0)

    def __str__(self):
        return f"Client - {self.turnover}"

    class Meta:
        permissions = [
            ("can_view_turnover", "Can view turnover"),
            ("can_edit_turnover", "Can edit turnover"),
        ]


class TeacherCalculation(models.Model):
    turnover = models.ForeignKey(Turnover, on_delete=models.CASCADE)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=1, null=True, default=0)
    hours_spent = models.DecimalField(max_digits=10, decimal_places=1, default=0, null=True)
    salary_teacher = models.DecimalField(max_digits=10, decimal_places=1, null=True, default=0)
    budget_teacher = models.DecimalField(max_digits=10, decimal_places=1, default=0, null=True)

    def __str__(self):
        return f"TeacherCalculation - {self.turnover}"

    class Meta:
        permissions = [
            ("can_view_turnover", "Can view turnover"),
            ("can_edit_turnover", "Can edit turnover"),
        ]


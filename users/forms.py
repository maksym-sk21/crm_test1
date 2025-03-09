from django import forms
from allauth.account.forms import SignupForm
from .models import User, Student, Teacher


class CustomSignupForm(SignupForm):
    ROLE_CHOICES = [
        ('student', 'Ученик'),
        ('teacher', 'Учитель'),
    ]

    name = forms.CharField(
        max_length=30,
        required=True,
        label="Имя",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    surname = forms.CharField(
        max_length=30,
        required=True,
        label="Фамилия",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    phone_number = forms.CharField(
        max_length=20,
        required=True,
        label="Номер телефона",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        required=True,
        label="Выберите роль",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def save(self, request):
        user = super().save(request)

        role = self.cleaned_data.get('role')
        user.name = self.cleaned_data.get('name')
        user.surname = self.cleaned_data.get('surname')
        user.save()

        phone_number = self.cleaned_data.get('phone_number')

        if role == 'student':
            user.is_student = True
            user.save()
            Student.objects.create(user=user, name=user.name, surname=user.surname, phone_number=phone_number)

        elif role == 'teacher':
            user.is_teacher = True
            user.save()
            Teacher.objects.create(user=user, name=user.name, surname=user.surname, phone_number=phone_number)

        return user

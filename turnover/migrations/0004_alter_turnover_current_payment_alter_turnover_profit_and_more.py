# Generated by Django 5.1.6 on 2025-02-28 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnover', '0003_rename_salary_elena_salary_salary_admin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turnover',
            name='current_payment',
            field=models.DecimalField(decimal_places=1, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='turnover',
            name='profit',
            field=models.DecimalField(decimal_places=1, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='turnover',
            name='total_hours',
            field=models.DecimalField(decimal_places=1, max_digits=10, null=True),
        ),
    ]

from django.db import models
from django.contrib.auth.models import AbstractUser

from django.db import models

class Department(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'department'
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'


class Employee(models.Model):
    EMPLOYMENT_TYPE_CHOICES = [
        ('FullTime', 'Full Time'),
        ('Intern', 'Intern'),
        ('Probation', 'Probation'),
    ]

    name = models.CharField(
        max_length=150,
        null=False,
        blank=False
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='employees'
    )
    join_date = models.DateField(
        null=True,
        blank=True
    )
    is_active = models.BooleanField(
        default=True
    )
    salary = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=False,
        blank=False
    )
    employment_type = models.CharField(
        max_length=50,
        choices=EMPLOYMENT_TYPE_CHOICES,
        null=False,
        blank=False
    )

    def __str__(self):
        return f"{self.name} ({self.get_employment_type_display()})"

    class Meta:
        db_table = 'employee'
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        
# class User():
#     email = models.EmailField(unique=True)
#     is_active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']

#     def __str__(self):
#         return self.email

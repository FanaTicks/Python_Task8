from django.db import models
class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=13, default='XXX-XXX-XXXX')
    EDUCATION_CHOICES = [
        ('спеціальна', 'Спеціальна'),
        ('середня', 'Середня'),
        ('вища', 'Вища'),
    ]
    education = models.CharField(max_length=10, choices=EDUCATION_CHOICES)
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True)
    position = models.ForeignKey('Position', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
class Department(models.Model):
    department_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13, default='XXX-XXX-XXXX')
    room_number = models.IntegerField()

    def __str__(self):
        return self.department_name

class Position(models.Model):
    position_name = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    bonus_percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.position_name

class Project(models.Model):
    project_name = models.CharField(max_length=255)
    completion_date = models.DateField()
    funding_amount = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.project_name

class ProjectExecution(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    start_date = models.DateField()

    def __str__(self):
        return f"{self.project.project_name} - {self.department.department_name}"

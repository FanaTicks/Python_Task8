from django.contrib import admin
from .models import Employee, Department, Position, Project, ProjectExecution

admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Position)
admin.site.register(Project)
admin.site.register(ProjectExecution)
# Register your models here.

from django.shortcuts import render
from .models import Employee, Department, Position, Project, ProjectExecution

def index(request):
    employees = Employee.objects.all()
    departments = Department.objects.all()
    positions = Position.objects.all()
    projects = Project.objects.all()
    executions = ProjectExecution.objects.all()
    context = {
        'employees': employees,
        'departments': departments,
        'positions': positions,
        'projects': projects,
        'executions': executions,
    }
    return render(request, 'myapp/index.html', context)
# Create your views here.

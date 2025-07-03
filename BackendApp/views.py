from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse

from BackendApp.models import Department, Employee
from BackendApp.serializers import DepartmentSerializer, EmployeeSerializer




 # Create your views here.

@csrf_exempt


# def department_list(request, id=None):
#     return JsonResponse({"message": f"Department list, ID: {id}"})

def department_list(request,id=0):
    if request.method == 'GET':
        departments = Department.objects.all()
        department_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(department_serializer.data, safe=False)

    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse(department_serializer.data, status=201)
        return JsonResponse(department_serializer.errors, status=400)

    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Department.objects.get(id=department_data['id'])
        department_serializer = DepartmentSerializer(department, data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse(department_serializer.data)
        return JsonResponse(department_serializer.errors, status=400)

    elif request.method == 'DELETE':
        department = Department.objects.get(id=id)
        department.delete()
        return JsonResponse({'message': 'Department deleted successfully!'}, status=204)
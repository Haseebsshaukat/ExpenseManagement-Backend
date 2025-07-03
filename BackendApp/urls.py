from django.urls import re_path  # use re_path for regex
from BackendApp import views

urlpatterns = [
    re_path(r'^department/$', views.department_list),
    # re_path(r'^department/(?P<id>[0-9]+)$', views.department_list),
    # re_path(r'^employee/$', views.employee_list),
    # re_path(r'^employee/(?P<id>[0-9]+)$', views.employee_list),
    # re_path(r'^employee/department/(?P<department_id>[0-9]+)$', views.employee_by_department),
    # re_path(r'^employee/salary/(?P<min_salary>[0-9]+)$', views.employee_by_salary),
    # re_path(r'^employee/salary/(?P<min_salary>[0-9]+)/(?P<max_salary>[0-9]+)$', views.employee_by_salary_range),
    # re_path(r'^employee/employment_type/(?P<employment_type>[a-zA-Z]+)$', views.employee_by_employment_type),
]

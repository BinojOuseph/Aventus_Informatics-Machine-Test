from django.urls import path
from employee.views import EmployeeData

urlpatterns=[
    path('employee',EmployeeData.as_view(),name='employee'),
    path('employee/<int:employee_id>',EmployeeData.as_view(),name='employee_update_delete'),
]
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from employee.models import EmployeeMaster 
from employee import serializers

# Create your views here.

class EmployeeData(APIView):
    serializer_class = serializers.EmployeeSerializer
    @extend_schema(
        tags=['Employee List API'],
    )
    def get(self, request, employee_id=None):
        if employee_id:
            try:
                employee = EmployeeMaster.objects.get(id=employee_id)
                serializer = self.serializer_class(employee)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except EmployeeMaster.DoesNotExist:
                return Response({'message': 'Employee with this id does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        employees = EmployeeMaster.objects.all()
        serializer = self.serializer_class(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
    tags=['Employee Create API'],
    ) 

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            # Check if the employee already exists
            if EmployeeMaster.objects.filter(email=request.data.get('email')).exists():
                return Response({'message': 'Employee with this email id already exists'}, status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            return Response({'message': 'Employee created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        tags=['Employee Update API'],
    )
    def put(self, request, employee_id):
        try:
            employee = EmployeeMaster.objects.get(id=employee_id)
        except EmployeeMaster.DoesNotExist:
            return Response({'message': 'Employee with this id does not exist'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(employee, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Employee data updated successfully'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        tags=['Employee Delete API'],
    )
    def delete(self, request, employee_id):
        try:
            employee = EmployeeMaster.objects.get(id=employee_id)
        except EmployeeMaster.DoesNotExist:
            return Response({'message': 'Employee with this id does not exist'}, status=status.HTTP_404_NOT_FOUND)

        employee.delete()
        return Response({'message': 'Employee deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
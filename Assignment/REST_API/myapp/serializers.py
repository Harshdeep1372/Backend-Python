from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
	class Meta:
		model=Employee
		fields=('id','emp_name','emp_dept_id','emp_dept_name','emp_salary')
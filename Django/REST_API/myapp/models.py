from django.db import models

# Create your models here.
class Employee(models.Model):
	emp_name=models.CharField(max_length=100,blank=True)
	emp_dept_id=models.PositiveIntegerField(blank=True)
	emp_dept_name=models.CharField(max_length=100,blank=True)
	emp_salary=models.PositiveIntegerField(blank=True)

	def __str__(self):
		return self.emp_name

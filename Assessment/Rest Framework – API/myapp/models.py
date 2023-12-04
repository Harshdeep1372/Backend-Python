from django.db import models

# Create your models here.
class Todo(models.Model):
	todo_list=models.CharField(max_length=100,blank=True)
	todo_detail_view=models.CharField(max_length=100,blank=True)
	todo_create=models.CharField(max_length=100,blank=True)
	todo_update=models.CharField(max_length=100,blank=True)
	todo_delete=models.CharField(max_length=100,blank=True)


	def __str__(self):
		return self.list

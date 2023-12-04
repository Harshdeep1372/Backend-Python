from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
	class Meta:
		model=Todo
		fields=('todo_list','todo_detail_view','todo_create','todo_update','todo_delete')
from django.contrib import admin
from .models import ProjectModel,ToDoItem,SubTasks
# Register your models here.
admin.register(ProjectModel,ToDoItem,SubTasks)
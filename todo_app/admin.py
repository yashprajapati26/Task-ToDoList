from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ['title','category','add_date','due_date','status']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['fullname','email',]


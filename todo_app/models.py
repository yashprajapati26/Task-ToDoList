from django.db import models
from django.utils import timezone

class User(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=30)

    def __str__(self):
      return self.email

class TodoList(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    title=models.CharField(max_length=100)
    description=models.TextField()
    category = models.CharField(max_length=50)
    add_date=models.DateTimeField(default=timezone.now)
    due_date=models.DateTimeField()
    status = models.BooleanField()
    
    def __str__(self):
      return self.title

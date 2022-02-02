from rest_framework import serializers
from . models import *  

class UserSerilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ToDoListSerilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TodoList
        fields = '__all__'
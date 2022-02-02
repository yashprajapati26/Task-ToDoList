from django.urls import path,include
from . import views 
from django.conf.urls.static import static
from django.conf import settings

#------routers------
from .views import *
from rest_framework import routers
from rest_framework.authtoken import views as v1
 
router = routers.DefaultRouter()
router.register(r'user',views.userviewsets)
router.register(r'Todolist',views.todolistviewsets)


urlpatterns = [

      #------------API urls-------------
      path('api/', include(router.urls)),
      path('api_auth/',include('rest_framework.urls',namespace='rest_framework')),

      # path('api-token-auth/', v1.obtain_auth_token, name='api-token-auth'),



      #-------------app urls--------------
      path('',views.login,name='login'),
      path('signup/',views.signup,name='signup'),

      path('todo/',views.index,name="index"),
      path('addToDo',views.addToDo,name="addToDo"),
      path('done_todo/<int:pk>',views.done_todo,name="done_todo"),
      path('remove_todo/<int:pk>',views.remove_todo,name="remove_todo"),
     
]
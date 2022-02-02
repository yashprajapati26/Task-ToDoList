from django.shortcuts import render,redirect
from .models import *
# Create your views here.

from rest_framework import viewsets
from .serilizers import *
from django.contrib.auth.models import User
 
 
class userviewsets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    print(queryset)
    serializer_class = UserSerilizer


class todolistviewsets(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    print(queryset)
    serializer_class = ToDoListSerilizer


#-------------- views here --------------------#

def login(request):
  if request.method == 'POST':  
    email = request.POST.get('email')
    pw = request.POST.get('pw')
    
    try:
        user = User.objects.get(email=email)
        if user.password != pw:
            msg = "Password is Wrrong."
            return render(request, 'login.html',{'msg':msg})

        request.session['email']=user.email
       
        request.session['name']=user.fullname
        return redirect('index')
    except:
        msg = "You are not Register! Do Signup ."
        return render(request,'login.html',{'msg':msg})
    
  else:
    return render(request,'login.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        pw = request.POST.get('pw')
        cpw = request.POST.get('cpw')

        if pw == cpw:
            User.objects.create(fullname=name, email=email, password=pw)
            return render(request,'login.html')
        else:
            msg = "Password and Confirm Password not Same !"
            return render(request,'signup.html',{'msg':msg})
    else:
        return render(request,'signup.html')


def index(request):
    try:
        user = User.objects.get(email = request.session['email'])
        todolist = TodoList.objects.filter(user=user).order_by('-id')
        return render(request,'index.html',{'todolist':todolist})

    except Exception as e:
        print("Exception:",e)
        return render(request,'index.html')


def addToDo(request):
    if request.method == 'POST':
        user = User.objects.get(email = request.session['email'])

        title = request.POST.get('title')
        description = request.POST.get('desc')
        category = request.POST.get('category')
        due_date = request.POST.get('duedate')

        todo = TodoList.objects.create(user=user,title=title,description=description,category=category,due_date=due_date,status=False)
        return redirect('index')
    else:
        return render(request,'addToDo.html')

def done_todo(request,pk):
    task = TodoList.objects.get(pk=pk)
    print(task)
    task.status = True
    task.save()
    return redirect('index')

def remove_todo(request,pk):
    task = TodoList.objects.get(pk=pk)
    print(task)
    task.delete()
    
    return redirect('index')

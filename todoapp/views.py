from django.shortcuts import redirect, render
from .models import TodoListItem
from .forms import UpdateTodoForm
from django.db import DatabaseError, transaction
from django.http import JsonResponse

# Create your views here.
def todoappview(request):
    todolist = TodoListItem.objects.filter(is_active=True)
    return render(request, 'todolist/todolist.html', {
        'todolist': todolist
    })


def update_todo(request):
    if request.method == "POST":
        form = UpdateTodoForm(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('/todo/')
    
    return render(request, 'todolist/todo_new.html')


def delete_todo(request, item):
    try:
        with transaction.atomic():
            todo = TodoListItem.objects.get(pk=item)
            todo.is_active = False
            todo.save()
            return redirect('/todo/')
    except DatabaseError:
        return JsonResponse(None, safe=False, status=400)


def ViewAllTodo(request):
    todo = TodoListItem.objects.all()
    return render(request, 'todolist/todoall.html', {
        'todoall': todo
    })

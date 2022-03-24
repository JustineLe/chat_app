from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import TodoListItem
from .forms import UpdateTodoForm

# Create your views here.
def todoappview(request):
    todolist = TodoListItem.objects.all()
    return render(request, 'todolist/todolist.html', {
        'todolist': todolist
    })


def update_todo(request):
    if request.method == "POST":
        form = UpdateTodoForm(request.POST)
        if form.is_valid():
            form.save()
        
        return HttpResponseRedirect('/todo/')


def delete_todo(request, item):
    todo = TodoListItem.objects.get(pk=item)
    todo.delete()
    return HttpResponseRedirect('/todo/')
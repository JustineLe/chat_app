from django.urls import path
from . import views

urlpatterns = [
    path('', views.todoappview, name='todo'),
    path('addTodoItem/', views.update_todo, name='update_todo'),
    path('deleteTodoItem/<int:item>', views.delete_todo, name='delete_todo'),
    path('viewAllTodo/', views.ViewAllTodo, name='viewall_todo'),
]
from django import forms
from .models import TodoListItem


class UpdateTodoForm(forms.ModelForm):
    class Meta:
        model = TodoListItem
        fields = '__all__'

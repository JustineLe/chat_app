from django.db import models

# Create your models here.
class TodoListItem(models.Model):
    content = models.CharField(max_length=255, null=False)

    class Meta:
        db_table = 'TodoList'
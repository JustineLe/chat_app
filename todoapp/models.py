from django.db import models
import datetime

# Create your models here.
class TodoListItem(models.Model):
    content = models.CharField(max_length=255, null=False)
    is_active = models.BooleanField(default=True)
    deadline = models.DateTimeField(default=(datetime.datetime.now() + datetime.timedelta(days=1)))
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=datetime.datetime.now())

    class Meta:
        db_table = 'TodoList'
from django.db import models

# Create your models here.

class Todo(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=230)
    completed = models.CharField(max_length=230)

def __str__(self) -> str:
    return f'<Todo {self.id} {self.description} {self.completed}>'


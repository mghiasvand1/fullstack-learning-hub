from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField(blank=True)
    priority = models.IntegerField(default=1)
    is_done = models.BooleanField()
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name='todos')

    def __str__(self) -> str:
        return f'{self.title} / Is Done: {self.is_done}'

    class Meta:
        db_table = 'todos'
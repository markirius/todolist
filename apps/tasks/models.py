import datetime
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Task(BaseModel):
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField(blank=True, null=True)
    due_date = models.DateField()
    done = models.BooleanField(default=False)

    class Meta:
        verbose_name = ('Task')
        verbose_name_plural = ('Tasks')
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def clean(self, *args, **kwargs):
        text = "the deadline must be equal to or greater than today's date"
        super(Task, self).clean(*args, **kwargs)
        if self.due_date < datetime.date.today():
            raise ValidationError(text)

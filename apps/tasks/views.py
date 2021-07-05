from django.views.generic import ListView
from django.views.generic.edit import CreateView

from apps.tasks.models import Task


class TaskList(ListView):
    model = Task
    paginate_by = 10
    context_object_name = "tasks"


class TaskCreate(CreateView):
    model = Task
    fields = '__all__'


class TaskUpdate():
    pass


class TaskDelete():
    pass

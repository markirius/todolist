from django.views.generic import ListView

from apps.tasks.models import Task


class TaskListView(ListView):
    model = Task
    paginate_by = 10
    context_object_name = "tasks"


class TaskCreate():
    pass


class TaskUpdate():
    pass


class TaskDelete():
    pass

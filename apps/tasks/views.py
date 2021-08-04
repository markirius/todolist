from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from apps.tasks.forms import TaskForm
from apps.tasks.models import Task


class TaskList(ListView):
    model = Task
    paginate_by = 10
    context_object_name = "tasks"


class TaskCreate(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class TaskUpdate(UpdateView):
    model = Task
    fields = "__all__"


class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')

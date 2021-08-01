from django.template.defaultfilters import slugify
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
    fields = ['title', 'content', 'due_date', 'done']
    form = TaskForm

    def form_valid(self, form):
        form = form.save(commit=False)
        title = form.cleaned_data['title']
        slug = slugify(title)
        content = form.cleaned_data['content']
        due_date = form.cleaned_data['due_date']
        done = form.cleaned_data['done']
        form.save()
        return super(form_valid, self).form_valid(form)



class TaskUpdate(UpdateView):
    model = Task
    fields = "__all__"


class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')

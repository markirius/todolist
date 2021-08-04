from django.forms import DateInput, DateTimeInput, ModelForm

from apps.tasks.models import Task


class DateTimeInput(DateTimeInput):
    input_type = 'date'


class TaskForm(ModelForm):

    class Meta:
        model = Task
        due_date = DateInput()
        fields = [
            'title',
            'content',
            'due_date',
            'done',
        ]
        labels = {
            'title': ('Title'),
            'content': ('Content'),
            'due_date': ('Due Date'),
            'done': ('Done')
        }
        widgets = {
            'due_date': DateInput(
                            format=('%m/%d/%Y'),
                            attrs={
                                'class': 'form-control',
                                'placeholder': 'Select a date',
                                'type': 'date',
                            }
                        ),
        }

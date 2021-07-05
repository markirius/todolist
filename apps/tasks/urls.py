from django.urls import path

from apps.tasks.views import TaskList, TaskCreate

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('create/', TaskCreate.as_view(), name='task_create'),
]

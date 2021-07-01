from django.urls import path

from apps.tasks.views import TaskListView

urlpatterns = [
    path('', TaskListView.as_view(), name='tasks'),
]

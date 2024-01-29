
from django.shortcuts import render


def task_list(request):
    tasks = ['Task 1', 'Task 2', 'Task 3']
    return render(request, 'tasks/task_list.html', {'tasks': tasks})
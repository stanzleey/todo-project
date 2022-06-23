from django.shortcuts import render
from django.http import Http404

# import class Task dari file todo/models.py
from .models import Task


# Membuat View untuk halaman daftar task
def index_view(request):
    # Mengambil semua data task
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    # parsing data task ke template todo/index.html dan merender nya
    return render(request, 'todo/index.html', context)


# Membuat View untuk halaman detail task
def detail_view(request, task_id):
    # Mengambil data task berdasarkan task ID
    try:
        task = Task.objects.get(pk=task_id)
        context = {
            'task': task
        }
    except Task.DoesNotExist:
        # Jika data task tidak ditemukan,
        # maka akan di redirect ke halaman 404 (Page not found).
        raise Http404("Task tidak ditemukan.")
    # parsing data task ke template todo/detail.html dan merendernya
    return render(request, 'todo/detail.html', context)
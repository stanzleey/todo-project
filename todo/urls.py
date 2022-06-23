from django.urls import path

# import View dari todo Application
from .views import index_view, detail_view

app_name = 'todo'
urlpatterns = [
    # route untuk halaman daftar task
    path('', index_view, name='index'),
  	
# route untuk halaman detail task
    path('<int:task_id>', detail_view, name='detail')
]

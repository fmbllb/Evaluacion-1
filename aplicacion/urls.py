from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),  # URL raíz apunta a la vista index
]
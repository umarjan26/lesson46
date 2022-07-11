from django.urls import path
from webapp.views import index, create_task, index_view, updates, delete

urlpatterns = [
    path('', index, name="index"),
    path('add/', create_task, name="add"),
    path('article/<int:pk>/', index_view, name="index_view"),
    path('updates/<int:pk>/update', updates, name="updates"),
    path('delete/<int:pk>/delete', delete, name="delete")
]

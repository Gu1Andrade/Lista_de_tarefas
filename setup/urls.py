from django.contrib import admin
from django.urls import path

from todos.views import TodoListView, TodoCreatView, TododoUpdateView, TodoDeleteview, TodoCompleteView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TodoListView.as_view(), name="todo_list"),
    path("create", TodoCreatView.as_view(), name="todo_create"),
    path("update/<int:pk>", TododoUpdateView.as_view(), name="todo_update"),
    path("delete/<int:pk>", TodoDeleteview.as_view(), name="todo_delete"),
    path("complete/<int:pk>", TodoCompleteView.as_view(), name="todo_complete"),
]

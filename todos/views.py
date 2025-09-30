from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

from .models import Todo


class TodoListView(ListView):
    model = Todo

class TodoCreatView(CreateView):
    model = Todo
    template_name = "todos/todo_form.html"
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")

class TododoUpdateView(UpdateView):
    model = Todo
    template_name = "todos/todo_form.html"
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")

class TodoDeleteview(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")

class TodoCompleteView(View):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.mark_has_complete()
        return redirect("todo_list")
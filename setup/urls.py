from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView

from todos.views import TodoListView, TodoCreatView, TododoUpdateView, TodoDeleteview, TodoCompleteView

urlpatterns = [
    path("admin/", admin.site.urls),
    
    # 1. Rota de Redirecionamento (Resolverá o problema do index.html)
    # Qualquer acesso à raiz (ex: "seusite.com/") será redirecionado para a rota 'todo_list'
    path("", RedirectView.as_view(pattern_name='todo_list', permanent=False), name='index'),

    # 2. Rota Real da Lista de Tarefas (agora precisa de um caminho, ex: "list/")
    path("list/", TodoListView.as_view(), name="todo_list"), 

    # As rotas de CRUD, agora corrigidas:
    path("create", TodoCreatView.as_view(), name="todo_create"),
    path("update/<int:pk>", TododoUpdateView.as_view(), name="todo_update"),
    path("delete/<int:pk>", TodoDeleteview.as_view(), name="todo_delete"),
    path("complete/<int:pk>", TodoCompleteView.as_view(), name="todo_complete"),
]

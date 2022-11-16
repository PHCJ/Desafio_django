from django.urls import path
from .views import ListaUsuarioView, UsuarioCreateView, UsuarioUpdateView, UsuarioDeleteView, UsuarioView
from usuario import views

urlpatterns = [
    path('', ListaUsuarioView.as_view(), name='usuario.index'),
    path('cadastrar', UsuarioCreateView.as_view(), name='usuario.novo'),
    path('editar/<int:pk>', UsuarioUpdateView.as_view(), name='usuario.editar'),
    path('excluir/<int:pk>', UsuarioDeleteView.as_view(), name='usuario.excluir'),
    path('dados', UsuarioView.as_view(), name='usuario.json'),
]
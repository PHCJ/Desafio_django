from django.views.generic import ListView,CreateView, UpdateView, DeleteView
from django.views import View
from usuario.models import Usuario
from django.http import HttpResponse
from .forms import UsuarioForm
import json
from django.core.serializers.json import DjangoJSONEncoder

class ListaUsuarioView(ListView):
    model = Usuario
    queryset = Usuario.objects.all().order_by('nomeUsuario')

    def get_queryset(self):
        queryset = super().get_queryset()
        filterName = self.request.GET.get('nomeBusca') or None

        if filterName:
            queryset = queryset.filter(nomeUsuario__contains=filterName)
        return queryset

class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    success_url = '/usuario'


class UsuarioUpdateView(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    success_url = '/usuario'

class UsuarioDeleteView(DeleteView):
    model = Usuario
    success_url = '/usuario'

class UsuarioView(View):
    def get(self, request):
        data = list(Usuario.objects.values())
        return HttpResponse(json.dumps(data,ensure_ascii=False,cls=DjangoJSONEncoder))
from typing import Any
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from .models import Especialidade
from django.urls import reverse_lazy

# Create your views here.
class EspecialidadeCreate(CreateView):
    model = Especialidade
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-especialidade')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Cadastro de Especialidade'
        context['botao'] = 'Cadastrar'
        return context

class EspecialidadeUpdate(UpdateView):
    model = Especialidade
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-especialidade')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Atualização de Especialidade'
        context['botao'] = 'Atualizar'
        return context

class EspecialidadeDelete(DeleteView):
    model = Especialidade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-especialidade')

class EspecialidadeList(ListView):
    model = Especialidade
    template_name = 'cadastros/listas/especialidade.html'

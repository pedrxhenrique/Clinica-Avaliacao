from django.urls import path
from .views import EspecialidadeCreate, EspecialidadeUpdate, EspecialidadeDelete, EspecialidadeList


urlpatterns = [
    path('cadastrar/especialidade/', EspecialidadeCreate.as_view(), name='cadastrar-especialidade'),
    path('editar/especialidade/<int:pk>/', EspecialidadeUpdate.as_view(), name='editar-especialidade'),
    path('excluir/especialidade/<int:pk>/', EspecialidadeDelete.as_view(), name='excluir-especialidade'),
    path('listar/especialidade/', EspecialidadeList.as_view(), name='listar-especialidade')
]
from django.db import models

# Create your models here.
class Especialidade(models.Model):
    nome = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        return "{}".format(self.nome)

class Medico(models.Model):
    nomeCompleto = models.CharField(max_length=100, null=False, verbose_name="Nome Completo")
    crm = models.CharField(max_length=10, unique=True, verbose_name = "CRM")
    especialidade = models.ForeignKey(Especialidade, on_delete=models.PROTECT)

    def __str__(self):
        return "{} - {}".format(self.nomeCompleto, self.crm)
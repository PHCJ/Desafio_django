from django.db import models

class Usuario(models.Model):
    nomeUsuario = models.CharField(max_length=150)
    dataNascimento = models.DateField(null=True)
    senha = models.CharField(max_length=10, blank=True)

    def __str__(self) -> str:
        return self.nomeUsuario

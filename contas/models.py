from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):

    PERFIS = (
        ('admin', 'Administrador'),
        ('secretaria', 'Secretaria'),
        ('professor', 'Professor'),
        ('responsavel', 'Responsável'),
    )

    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    tipo = models.CharField(
        max_length=20,
        choices=PERFIS
    )

    def __str__(self):

        if self.usuario:
            return f'{self.usuario.username} - {self.tipo}'

        return self.tipo
    tipo = models.CharField(
        max_length=20,
        choices=PERFIS
    )

    def __str__(self):

        if self.usuario:
            return f'{self.usuario.username} - {self.tipo}'

        return self.tipo
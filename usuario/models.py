from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    senha = models.CharField(max_length=64)
    ativo = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
    

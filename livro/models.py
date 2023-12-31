from tabnanny import verbose
from django.db import models
from datetime import date, datetime
import usuario
from usuario.models import Usuario
import datetime 

class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome 

class Livros(models.Model):
    img = models.ImageField(upload_to='capa_livro', null=True, blank=True)
    nome = models.CharField(max_length = 100)
    autor = models.CharField(max_length = 30)
    data_cadastro = models.DateField(default= date.today)
    emprestado = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    

    class Meta: # a classe meta dentro de uma classe faz com que seja possivel alterar o nome da classe para que a visualização do admin não fique com duas letras s no final
        verbose_name = 'Livro' 

    def __str__(self):
        return self.nome

class Emprestimos(models.Model):
    choices = (
        ('P', 'Pessimo'),
        ('R', 'Ruim'),
        ('B', 'Bom'),
        ('O', 'Otimo')
    )
    nome_emprestado = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, blank=True, null=True)
    data_emprestimo = models.DateField(default=datetime.datetime.now())
    data_devolucao = models.DateField(blank=True, null=True)
    livro = models.ForeignKey(Livros, on_delete=models.SET_NULL, null=True)
    avaliacao = models.CharField(max_length=1, choices=choices, blank=True, null=True)

    def __str__(self):
        if self.nome_emprestado:
            return f'{self.nome_emprestado} / {self.livro}'
        else:
            return f'{self.nome_emprestado_anonimo} / {self.livro}'



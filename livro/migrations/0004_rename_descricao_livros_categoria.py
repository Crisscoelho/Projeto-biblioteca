# Generated by Django 4.1.1 on 2022-10-01 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0003_categoria_livros_descricao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livros',
            old_name='descricao',
            new_name='categoria',
        ),
    ]
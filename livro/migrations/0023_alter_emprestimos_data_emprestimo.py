# Generated by Django 4.2.6 on 2023-10-31 00:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0022_alter_emprestimos_data_emprestimo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimos',
            name='data_emprestimo',
            field=models.DateField(default=datetime.datetime(2023, 10, 30, 21, 5, 56, 425965)),
        ),
    ]

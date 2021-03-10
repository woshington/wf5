# Generated by Django 3.1.7 on 2021-03-10 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Novo'), (2, 'Aprovado'), (3, 'Cancelado')], db_column='flStatus', default=1, verbose_name='status'),
        ),
    ]

# Generated by Django 3.1.7 on 2021-03-10 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20210309_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='code',
            field=models.CharField(db_column='cdProjeto', max_length=20, unique=True, verbose_name='codigo'),
        ),
    ]
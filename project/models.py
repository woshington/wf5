from django.db import models
from accounts.models import User

# Create your models here.

class Project(models.Model):
    id = models.AutoField(primary_key=True, db_column='idProjeto')
    code = models.CharField(
        "codigo", max_length=20, null=False, db_column='cdProjeto'
    )
    name = models.CharField(
        "nome", max_length=80, null=False, db_column='nmProjeto'
    )
    description = models.TextField(
        "descrição", null=True, db_column='deProjeto'
    )
    created_at = models.DateTimeField(
        'criado em', auto_now_add=True
    )
    approval_date = models.DateTimeField(
        "data aprovação", null=True, db_column='dtAprovacao'
    )
    cancellation_date = models.DateTimeField(
        "data cancelamento", null=True, db_column='dtCancelamento'
    )
    status = models.PositiveSmallIntegerField(
        "status", null=False, db_column="flStatus"
    )
    user = models.ForeignKey(
        User, verbose_name="usuario", db_column="nuUsuario", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"
        db_table = "eptfProjeto"


class Management(models.Model):
    id = models.AutoField(primary_key=True, db_column='idGerenciamento')
    budget = models.DecimalField(
        "orçamento", null=False, max_digits=9, decimal_places=2, 
        db_column="vlOrcamento"
    )
    spent = models.DecimalField(
        "Gasto", null=False, max_digits=9, decimal_places=2, 
        db_column="vlGasto"
    )
    project = models.ForeignKey(
        Project, verbose_name="projeto", db_column="nuProjeto", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Gerenciamento"
        verbose_name_plural = "Gerenciamentos"
        db_table = "egstGerenciamento"
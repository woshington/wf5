from django.db import models
from accounts.models import User
from django.db.models import Sum

# Create your models here.


class Project(models.Model):
    CHOICES_STATUS = (
        (1, 'Novo'),
        (2, 'Aprovado'),
        (3, 'Cancelado'),
    )
    id = models.AutoField(primary_key=True, db_column='idProjeto')
    code = models.CharField(
        "codigo", max_length=20, null=False, unique=True, db_column='cdProjeto'
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
        "status", null=False, choices=CHOICES_STATUS,
        db_column="flStatus", default=1
    )
    user = models.ForeignKey(
        User, verbose_name="usuario", db_column="nuUsuario",
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"
        db_table = "eptfProjeto"
    
    def __str__(self):
        return self.name

    @property
    def balanced(self):
        """
        Return: available budget or zero when status is not approved
        """
        if self.status != 2:
            return 0
        management = self.management_set.aggregate(
            budget_value=Sum('budget'), spent_value=Sum('spent')
        )
        return management['budget_value'] - management['spent_value']


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
        Project, verbose_name="projeto", db_column="nuProjeto",
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Gerenciamento"
        verbose_name_plural = "Gerenciamentos"
        db_table = "egstGerenciamento"

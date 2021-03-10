from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
# Create your models here.


# Customizando o gerenciador do nosso model de autenticação
# Com essa customização podemos invocar os métodos createuser
class UserManager(BaseUserManager):

    def _create_user(self, name, email, password, profile, **extra_fields):
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            name=name, email=email,
            profile=profile,
            last_login=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, name=None, email=None, profile=None, password=None, **extra_fields):
        return self._create_user(name, email, password, profile, **extra_fields)


class User(AbstractBaseUser):
    PROFILE_CHOICES = (
        (1, 'Junior'),
        (2, 'Pleno'),
        (3, 'Sênior'),
    )

    id = models.AutoField(primary_key=True, db_column='idUsuario')
    name = models.CharField(
        "Usuario", max_length=80, null=False, db_column='nmUsuario'
    )
    email = models.EmailField(
        "email", max_length=50, null=False, unique=True, db_column='nmEmail'
    )
    password = models.CharField(
        "senha", max_length=30, null=False, db_column='nmSenha'
    )
    profile = models.PositiveSmallIntegerField(
        "perfil", null=False, choices=PROFILE_CHOICES, db_column='nuProfile'
    )
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    objects = UserManager()

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        db_table = "ecdtUsuario"

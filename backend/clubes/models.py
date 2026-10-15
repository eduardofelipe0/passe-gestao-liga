from django.db import models
from decimal import Decimal
from .utils import normalizar_nome

# Create your models here.

class Clube(models.Model):
    class Formacao(models.TextChoices):
        TRES_UM = "3-1", "3-1"
        DOIS_DOIS = "2-2", "2-2"
        DOIS_UM_UM = "2-1-1", "2-1-1"
        UM_DOIS_UM = "1-2-1", "1-2-1"

    nome = models.CharField(max_length=60)
    nome_normalizado = models.CharField(
        max_length=60,
        unique=True,
        editable=False,
    )
    sigla = models.CharField(max_length=3, unique=True)
    caixa = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal("300.00"),
    )
    formacao = models.CharField(
        max_length=5,
        choices=Formacao.choices,
        null=True,
        blank=True,
    )
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "clubes"
        
    def save(self, *args, **kwargs):
        self.nome_normalizado = normalizar_nome(self.nome)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome} ({self.sigla})"

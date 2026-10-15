from django.db import models

# Create your models here.

class Contrato(models.Model):
    class Situacao(models.TextChoices):
        ATIVO = "ATIVO", "Ativo"
        ENCERRADO = "ENCERRADO", "Encerrado"
        RESCINDIDO = "RESCINDIDO", "Rescindido"

    jogador = models.ForeignKey(
        "jogadores.Jogador",
        on_delete=models.PROTECT,
        related_name="contratos",
    )

    clube = models.ForeignKey(
        "clubes.Clube",
        on_delete=models.PROTECT,
        related_name="contratos",
    )

    valor_compra = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )

    fidelidade_ate = models.DateTimeField()

    situacao = models.CharField(
        max_length=12,
        choices=Situacao.choices,
        default=Situacao.ATIVO,
    )

    iniciado_em = models.DateTimeField(auto_now_add=True)

    encerrado_em = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "contratos"

    def __str__(self):
        return f"Contrato {self.pk} - {self.jogador.nome}"


class Transacao(models.Model):
    class Tipo(models.TextChoices):
        COMPRA = "COMPRA", "Compra"
        VENDA = "VENDA", "Venda"

    clube = models.ForeignKey(
        "clubes.Clube",
        on_delete=models.PROTECT,
        related_name="transacoes",
    )

    jogador = models.ForeignKey(
        "jogadores.Jogador",
        on_delete=models.PROTECT,
        related_name="transacoes",
    )

    nome_jogador = models.CharField(max_length=100)

    tipo = models.CharField(
        max_length=6,
        choices=Tipo.choices,
    )

    valor = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )

    taxa = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )

    multa = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )

    lucro = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        null=True,
        blank=True,
    )

    variacao_caixa = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )

    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "transacoes"

    def __str__(self):
        return f"{self.tipo} - {self.nome_jogador}"

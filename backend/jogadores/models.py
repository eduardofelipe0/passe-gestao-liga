from django.db import models

# Create your models here.

class Jogador(models.Model):
    class Posicao(models.TextChoices):
        GOLEIRO = "GOL", "Goleiro"
        ZAGUEIRO = "ZAG", "Zagueiro"
        LATERAL = "LAT", "Lateral"
        MEIO_CAMPO = "MEI", "Meio-campo"
        ATACANTE = "ATA", "Atacante"

    class Condicao(models.TextChoices):
        APTO = "APTO", "Apto"
        MAL_CONDICIONADO = "MAL_CONDICIONADO", "Mal condicionado"
        DOENTE = "DOENTE", "Doente"

    nome = models.CharField(max_length=100)

    posicao = models.CharField(
        max_length=3,
        choices=Posicao.choices,
    )

    agilidade = models.IntegerField()
    idade = models.IntegerField()

    valor_base = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )

    condicao = models.CharField(
        max_length=20,
        choices=Condicao.choices,
        default=Condicao.APTO,
    )

    clube = models.ForeignKey(
        "clubes.Clube",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="jogadores",
    )

    velocidade = models.IntegerField()
    finalizacao = models.IntegerField()
    passe = models.IntegerField()
    drible = models.IntegerField()
    defesa = models.IntegerField()
    fisico = models.IntegerField()

    potencial = models.IntegerField()

    excluido_em = models.DateTimeField(
        null=True,
        blank=True,
    )

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "jogadores"

    def __str__(self):
        return f"{self.nome} - {self.posicao}"

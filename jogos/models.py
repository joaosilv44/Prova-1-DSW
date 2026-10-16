from django.db import models

class Modalidade(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    max_atletas = models.PositiveIntegerField()
    
    class TipoModalidadeChoices(models.TextChoices):
        COLETIVO = "C0", ("Coletivo")
        INDIVIDUAL = "IN", ("Individual")

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ["nome"]

class Equipe(models.Model):
    tecnico = models.OneToOneField(
        "Tecnico",
        on_delete=models.CASCADE,
        related_name="equipes",
    )

    nome = models.CharField(max_length=100, unique=True)
    curso = models.CharField(max_length=100)
    cor = models.CharField(max_length=6)
    criada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ["nome"]

class Tecnico(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=14)

    def __str__(self):
        return self.nome

class Atleta(models.Model):
    equipe = models.ForeignKey(
        "Equipe",
        on_delete=models.PROTECT,
        related_name="equipe",
    )

    modalidade = models.ManyToManyField(
        "Modalidade",
        related_name="atletas",
    )

    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=50, unique=True)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ["nome"]
from django.db import models


class Doctor(models.Model):
    nome = models.CharField(max_length=200)
    especialidade = models.CharField(max_length=200)
    crm = models.CharField(max_length=50)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    visualizacoes = models.IntegerField(default=0) # Coloquei add visualizações manualmente para testar o filtro

    descricao = models.TextField(
        null=True, default="Não informado", help_text="Descreva a pessoa do médico."
    )

    patologias = models.TextField(
        null=True,
        default="Não informado",
        help_text="Lista de patologias, separadas por vírgula.",
    )

    atendimento = models.TextField(
        null=True,
        default="Não informado",
        help_text="Grupos atendidos (ex: Crianças, Adolescentes, Adultos e Idosos).",
    )

    convenio = models.BooleanField(default=False)

    retorno_acompanhamento = models.CharField(
        default="Não informado",
        max_length=100,
        blank=True,
        null=True,
        help_text="Ex: 'Retorno em até 30 dias'",
    )

    experiencia_prescricao = models.CharField(
        default="Não informado",
        max_length=500,
        blank=True,
        null=True,
        help_text="Ex: 'Sim' ou 'Não' ou 'Não informado'",
    )

    formacao = models.TextField(
        default="Não informado",
        blank=True,
        null=True,
        help_text="Onde se formou e suas especialidades",
    )

    foto = models.ImageField(upload_to="doctors/", blank=True, null=True)

    preco_consulta = models.DecimalField(
        max_digits=8, decimal_places=2, default="00.00"
    )

    duracao_consulta = models.IntegerField(
        help_text="Duração da consulta em minutos", default="00"
    )

    def __str__(self):
        return self.nome

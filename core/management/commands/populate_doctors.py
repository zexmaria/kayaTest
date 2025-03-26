import os
import random
import subprocess
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from core.models import Doctor
from decimal import Decimal


class Command(BaseCommand):

    help = f'\033[32m❗❗❗Adiciona médicos fictícios ao banco de dados❗❗❗\033[0m'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Número de médicos a serem criados e adicionados')

    def handle(self, *args, **kwargs):
        total = kwargs['total']

        nomes = [
            'Dra. Amanda Sousa',
            'Dra. Fernanda Paiva',
            'Dra. Renata Costa',
            'Dra. Raquel Furtado',
            'Dra. Maria Medeiros',
            'Dra. Paula Moura',
            'Dra. Marcela Ferreira',
            'Dra. Alice Viana',
            'Dra. Janaina Duarte',
            'Dra. Tatiane Macedo',
            'Dra. Gisele Dutra',
            'Dra. Vanessa Araujo',
        ]

        especialidades = [
            'CLÍNICO GERAL',
            'MEDICINA DE FAMÍLIA E COMUNIDADE',
            'MEDICINA PREVENTIVA E SOCIAL',
            'MEDICINA DO TRABALHO',
            'MEDICINA FUNCIONAL INTEGRATIVA',
            'DENTISTA',
            'MEDICINA INTEGRATIVA',
            'RADIOLOGIA E DIAGNÓSTICO POR IMAGEM',
            'MEDICINA DE FAMÍLIA E COMUNIDADE - RQE N21312',
            'GENERALISTA | MEDICINA ENDOCANABINOIDE',
        ]

        cidade = 'São Paulo'
        estado = 'SP'

        base_dir = os.path.dirname(os.path.abspath(__file__))
        img_folder = os.path.join(base_dir, 'img_doctors')
        add_fotos = [
            'prancheta1.jpg',
            'prancheta2.jpg',
            'prancheta3.jpg',
            'prancheta4.jpg',
            'prancheta5.jpg',
            'prancheta6.jpg',
            'prancheta7.jpg',
            'prancheta8.jpg',
            'prancheta9.jpg',
            'prancheta10.jpg',
            'prancheta11.jpg',
            'prancheta12.jpg',
        ]

        for _ in range(total):
            nome = random.choice(nomes)
            especialidade = random.choice(especialidades)
            crm = ''.join(random.choices('0123456789', k=5))
            visualizacoes = random.randint(1, 75)
            foto_nome = random.choice(add_fotos)

            foto_caminho = os.path.join(img_folder, foto_nome)

            valores=[310.00, 580.00, 420,00,
                  99.99, 250.00, 200,
                  950.00, 125,00.00, 280,
                  330.00, 540.00, 300.00,
                  ]
            valor_escolhido = Decimal(random.choice(valores))

            try:
                with open(foto_caminho, 'rb') as img_file:
                    foto_content = ContentFile(img_file.read(), name=foto_nome)

                doctor = Doctor.objects.create(
                    nome=nome,
                    especialidade=especialidade,
                    crm=crm,
                    cidade=cidade,
                    estado=estado,
                    visualizacoes=visualizacoes,
                    descricao='Médica formada pela Unesp Botucatu, com especialização em psicanálise '
                              'e ênfase no tratamento da dor crônica. Pós-graduada em Cannabis Sativa '
                              'pela Sbec e certificada internacionalmente em cannabis pela WeCann Academy. '
                              'Completou a Capacitação em Cannabis Medicinal pela USP-SP e Unicamp.',
                    patologias='Dor Crônica, Alzheimer, TEA, Depressão, Ansiedade, Insônia, Enxaqueca, '
                               'Fibromialgia, Parkinson',
                    atendimento='Crianças, Adolescentes, Adultos e Idosos',
                    foto=foto_content,
                    preco_consulta=valor_escolhido
                )
                subprocess.check_call("", shell=True)
                print(f"\033[32m✅ {doctor.nome} criado(a) com sucesso!\033[0m")
            except subprocess.CalledProcessError:
                print("❌ Erro ao criar usuário(s)")

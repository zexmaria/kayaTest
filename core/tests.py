import pytest
from django.urls import reverse
from django.test import Client
from .models import Doctor

@pytest.fixture
def client():
    return Client()

@pytest.fixture
def doctor():
    return Doctor.objects.create(
        nome="Dr. João Silva",
        especialidade="Clínico Geral",
        crm="123456-SP",
        cidade="São Paulo",
        estado="SP",
        visualizacoes=10,
        descricao="Especialista em medicina canabinoide",
        patologias="Ansiedade, Depressão",
        atendimento="Adultos",
        convenio=True,
        retorno_acompanhamento="Retorno em até 30 dias",
        experiencia_prescricao="Sim",
        formacao="Universidade de São Paulo",
        preco_consulta=350.00,
        duracao_consulta=60,
    )

def test_doctor_profile_view(client, doctor):
    url = reverse("core:doctor_profile", args=[doctor.id])
    response = client.get(url)
    assert response.status_code == 200
    assert doctor.nome in response.content.decode()

def test_doctor_list_view(client, doctor):
    url = reverse("core:index")
    response = client.get(url)
    assert response.status_code == 200
    assert doctor.nome in response.content.decode()

def test_doctor_list_filter_by_especialidade(client, doctor):
    url = reverse("core:index") + "?especialidade=Clínico Geral"
    response = client.get(url)
    assert response.status_code == 200
    assert doctor.nome in response.content.decode()

def test_doctor_list_order_by_menor_valor(client, doctor):
    url = reverse("core:index") + "?ordenar=menor_valor"
    response = client.get(url)
    assert response.status_code == 200
    assert doctor.nome in response.content.decode()

def test_doctor_list_order_by_maior_valor(client, doctor):
    url = reverse("core:index") + "?ordenar=maior_valor"
    response = client.get(url)
    assert response.status_code == 200
    assert doctor.nome in response.content.decode()

def test_doctor_list_order_by_visualizacoes(client, doctor):
    url = reverse("core:index") + "?ordenar=visualizacoes"
    response = client.get(url)
    assert response.status_code == 200
    assert doctor.nome in response.content.decode()

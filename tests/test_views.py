import pytest
from core.models import Doctor
from django.urls import reverse


@pytest.fixture
def doctor():
    return Doctor.objects.create(
        nome="Dr. José Gomes",
        especialidade="Dentista",
        crm="123456",
        cidade="São Paulo",
        estado="SP",
        visualizacoes=10,
        descricao="Especialista em medicina canabinoide",
        preco_consulta=350.00,
        duracao_consulta=60,
    )


@pytest.fixture
def multiple_doctors():
    doctor1 = Doctor.objects.create(
        nome="Dr. João Silva",
        especialidade="Clínico Geral",
        crm="123457",
        cidade="São Paulo",
        estado="SP",
        visualizacoes=25,
        preco_consulta=350.00,
        duracao_consulta=45,
    )
    doctor2 = Doctor.objects.create(
        nome="Dra. Maria Oliveira",
        especialidade="Dermatologia",
        crm="123458",
        cidade="São Paulo",
        estado="SP",
        visualizacoes=25,
        preco_consulta=350.00,
        duracao_consulta=45,
    )
    doctor3 = Doctor.objects.create(
        nome="Dr. Pedro Martins",
        especialidade="Dentista",
        crm="123459",
        cidade="São Paulo",
        estado="SP",
        visualizacoes=25,
        preco_consulta=350.00,
        duracao_consulta=45,
    )
    return [doctor1, doctor2, doctor3]


@pytest.mark.django_db
def test_if_doctor_profile_view_return_200(client, doctor):
    url = reverse("core:doctor_profile", args=[doctor.id])
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_if_doctor_profile_view_not_found_return_404(client):
    url = reverse("core:doctor_profile", args=[999999])
    response = client.get(url)
    assert response.status_code == 404


@pytest.mark.django_db
def test_if_without_filters_returns_all_doctors(client, multiple_doctors):
    response = client.get(multiple_doctors)

# NÃO FINALIZADO 20/03/2025 - 10:57
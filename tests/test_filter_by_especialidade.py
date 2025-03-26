import pytest
from core.models import Doctor


@pytest.fixture
def doctor():
    return[
        Doctor.objects.create(
            nome="Dr. João Silva",
            especialidade="Clínico Geral",
            crm="123456",
            cidade="São Paulo",
            estado="SP",
            visualizacoes=10,
            descricao="Especialista em medicina canabinoide",
            preco_consulta=350.00,
            duracao_consulta=60,
        ),
        Doctor.objects.create(
            nome="Dra. Ana Carla",
            especialidade="Clínico Geral",
            crm="123456",
            cidade="São Paulo",
            estado="SP",
            visualizacoes=10,
            descricao="Especialista em medicina canabinoide",
            preco_consulta=350.00,
            duracao_consulta=60,
        ),
        Doctor.objects.create(
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
    ]


@pytest.mark.django_db
def test_filter_by_especialidade_clinico_geral(doctor):
    assert doctor[0].especialidade == 'Clínico Geral'


@pytest.mark.django_db
def test_filter_if_multiples_especialidades_are_allowed(doctor):
    clinicos = Doctor.objects.filter(especialidade="Clínico Geral")
    assert clinicos.count() == 2
    assert doctor[0].especialidade == 'Clínico Geral'
    assert doctor[1].especialidade == 'Clínico Geral'


@pytest.mark.django_db
def test_filter_by_especialidade_dentista(doctor):
    dentistas = Doctor.objects.filter(especialidade="Dentista")
    assert dentistas.count() == 1
    assert doctor[2].especialidade == 'Dentista'


@pytest.mark.django_db
def test_filter_by_especialidade_nao_existente():
    dermatologistas = Doctor.objects.filter(especialidade="Dermatologista")
    assert dermatologistas.count() == 0

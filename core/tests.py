import os
from django.core.management import call_command
from django.test import TestCase
from core.models import Doctor

class TestScriptPopulateDoctors(TestCase):

    def test_if_5_doctors_are_created(self):

        call_command('populate_doctors', 5)  # Substitua pelo nome real do comando
        assert doctor.objects.count(), 5

    def test_if_atributes_is_not_empty(self):
        # Verifica se os médicos foram criados com os atributos corretos
        doctor = Doctor.objects.first()
        #assert Doctor.nome(len) == 1
        self.assertIsNotNone(doctor.especialidade)
        self.assertIsNotNone(Doctor.crm)
        self.assertIsNotNone(Doctor.cidade)
        self.assertIsNotNone(Doctor.estado)
        self.assertIsNotNone(Doctor.preco_consulta)



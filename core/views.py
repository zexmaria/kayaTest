from django.shortcuts import render, get_object_or_404
from .models import Doctor
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render


def doctor_profile(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    return render(request, "core/doctor_profile.html", {"doctor": doctor})


class DoctorListView(APIView):
    def get(self, request):
        doctors = Doctor.objects.all()

        especialidade = request.GET.get("especialidade")
        if especialidade:
            doctors = doctors.filter(especialidade__icontains=especialidade)

        ordenar = request.GET.get("ordenar")
        if ordenar == "menor_valor":
            doctors = doctors.order_by("preco_consulta")
        elif ordenar == "maior_valor":
            doctors = doctors.order_by("-preco_consulta")
        elif ordenar == "visualizacoes":
            doctors = doctors.order_by("-visualizacoes")

        context = {
            "doctors": doctors,
            "especialidade_ativa": especialidade,
            "ordenar_ativo": ordenar,
        }
        return render(request, "core/index.html", context)

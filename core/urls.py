from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="index"),
    path('medicos/<int:doctor_id>/perfil/', views.doctor_profile, name='doctor_profile'),
]

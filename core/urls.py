from django.urls import path
from . import views
from .views import *

app_name = "core"

urlpatterns = [
    path('', DoctorListView.as_view(), name='index'),
    path('medicos/<int:doctor_id>/perfil/', views.doctor_profile, name='doctor_profile'),

]

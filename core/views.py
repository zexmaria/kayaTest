from django.shortcuts import render, get_object_or_404
from .models import Doctor

def doctor_profile(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    return render(request, 'core/doctor_profile.html', {'doctor': doctor})

def doctor(request):
    doctor = Doctor.objects.all()
    return render(request, 'index.html', {'medicos': doctor})

def home(request):
    doctors = Doctor.objects.all()
    return render(request, 'core/index.html', {'doctors': doctors})
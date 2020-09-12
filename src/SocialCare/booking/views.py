from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from .models import Hospital, Department, Doctor, Token, Patient
from .serializers import HospitalSerializer, DepartmentSerializer, DoctorSerializer, TokenSerializer, PatientSerializer

# Create your views here.
def booking_view(request, *args, **kwargs):
	#return HttpResponse('<h1>Booking</h1>')
	return render(request, "booking/booking.html", {})

def hospital_view(request, hospital_id, *args, **kwargs):
	#return HttpResponse('<h1>Booking</h1>')
	return render(request, "booking/hospital.html", {'hospital_id': hospital_id})


class HospitalViewSet(viewsets.ModelViewSet):
	queryset = Hospital.objects.all().order_by('name')
	serializer_class = HospitalSerializer
	#permission_classes = [permissions.IsAuthenticatedOrReadOnly]
	permission_classes = []

class DepartmentViewSet(viewsets.ModelViewSet):
	queryset = Department.objects.all().order_by('name')
	serializer_class = DepartmentSerializer
	#permission_classes = [permissions.IsAuthenticatedOrReadOnly]
	permission_classes = []

class DoctorViewSet(viewsets.ModelViewSet):
	queryset = Doctor.objects.all().order_by('name')
	serializer_class = DoctorSerializer
	#permission_classes = [permissions.IsAuthenticatedOrReadOnly]
	permission_classes = []

class PatientViewSet(viewsets.ModelViewSet):
	queryset = Patient.objects.all().order_by('name')
	serializer_class = PatientSerializer
	#permission_classes = [permissions.IsAuthenticatedOrReadOnly]
	permission_classes = []

class TokenViewSet(viewsets.ModelViewSet):
	queryset = Token.objects.all().order_by('token_number')
	serializer_class = TokenSerializer
	#permission_classes = [permissions.IsAuthenticatedOrReadOnly]
	permission_classes = []
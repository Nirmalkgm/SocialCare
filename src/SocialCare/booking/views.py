from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def booking_view(request, *args, **kwargs):
	#return HttpResponse('<h1>Booking</h1>')
	return render(request, "booking/booking.html", {})

def hospital_view(request, hospital_id, *args, **kwargs):
	#return HttpResponse('<h1>Booking</h1>')
	return render(request, "booking/hospital.html", {'hospital_id', hospital_id})
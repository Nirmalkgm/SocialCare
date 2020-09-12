from .views import booking_view, hospital_view
from django.urls import path

urlpatterns = [
	path('', booking_view, name='booking'),
	path('<hospital_id>', hospital_view, name='hospital'),
]
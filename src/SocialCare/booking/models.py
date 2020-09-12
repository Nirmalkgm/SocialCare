from django.db import models

# Create your models here.
class Hospital(models.Model):
	hospital_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=64)
	phone = models.CharField(max_length=15)
	email = models.CharField(max_length=64)
	address = models.CharField(max_length=128)
	city = models.CharField(max_length=64)
	state = models.CharField(max_length=64)
	country = models.CharField(max_length=64)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name

class Department(models.Model):
	department_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=32)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name

class Doctor(models.Model):
	doctor_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=64)
	specializtions = models.CharField(max_length=64)
	department = models.ForeignKey(Department, on_delete=models.PROTECT)
	hospital = models.ForeignKey(Hospital, on_delete=models.PROTECT)

	class Meta:
		ordering = ['name']
	
	def __str__(self):
		return self.name
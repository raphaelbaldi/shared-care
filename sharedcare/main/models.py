from django.db import models
from django.contrib.auth.models import User

# User profile, connected to an actual user in the system
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.TextField(max_length=11, blank=False)
    birth_date = models.DateField(null=True, blank=True)

class Allergy(models.Model):
    name = models.TextField(max_length=100, blank=False)
    description = models.TextField(max_length=500, blank=True)
    symptoms = models.TextField(max_length=500, blank=True)

class Doctor(models.Model):
    name = models.TextField(max_length=100, blank=False)
    specialty = models.TextField(max_length=50, blank=False)

class MedicalAppointment(model.Model):
    person = models.ForeignKey(Elderly, related_name='appointment')
    doctor = models.ForeignKey(Doctor, related_name='appointment')
    description = models.TextField(max_length=500, blank=True)
    date = models.DateTimeField(null=False, blank=False)

class Food(model.Model):
    name = models.TextField(max_length=100, blank=False)

class Elderly(models.Model):
    name = models.TextField(max_length=100, blank=False)
    cpf = models.TextField(max_length=11, blank=False)
    birth_date = models.DateField(null=True, blank=True)
    allergies = models.ManyToManyField(Allergy, blank=True)
    caretaker = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, blank=True, null=True)
    medical_appointments = models.ManyToManyField('Doctor', through='MedicalAppointment', related_name='person')

from enum import Enum
from django.db import models
from django.contrib.auth.models import User


# User profile, connected to an actual user in the system
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11, blank=False)
    birth_date = models.DateField(null=True, blank=True)


class Allergy(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=500, blank=True)
    symptoms = models.TextField(max_length=500, blank=True)


class Doctor(models.Model):
    name = models.CharField(max_length=100, blank=False)
    specialty = models.CharField(max_length=50, blank=False)


class MedicalAppointment(models.Model):
    person = models.ForeignKey('Elderly', related_name='appointment', on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, related_name='appointment', on_delete=models.CASCADE)
    description = models.TextField(max_length=500, blank=True)
    date = models.DateTimeField(null=False, blank=False)


class Food(models.Model):
    name = models.CharField(max_length=100, blank=False)


class MealType(Enum):
    CafeDaManha = "Café da Manhã"
    Lanche = "Lanche"
    Almoco = "Almoço"
    Janta = "Janta"
    Ceia = "Ceia"


class Meal(models.Model):
    type = models.CharField(
        max_length=5,
        choices=[(tag, tag.value) for tag in MealType],
        null=False,
        blank=False
    )
    date = models.DateTimeField(null=False, blank=False)
    foods = models.ManyToManyField(Food, blank=True)


class Medicine(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=500, blank=True, null=True)


class Prescription(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    startDate = models.DateField(blank=False, null=False)
    endDate = models.DateField(blank=True, null=True)
    frequency = models.PositiveIntegerField() # In hours


class ConsumedMedicine(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(blank=False, null=False)
    date = models.DateTimeField(blank=False, null=False)


class Elderly(models.Model):
    name = models.CharField(max_length=100, blank=False)
    cpf = models.CharField(max_length=11, blank=False)
    birth_date = models.DateField(null=True, blank=True)
    caretaker = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, blank=True, null=True)
    allergies = models.ManyToManyField(Allergy, blank=True)
    medical_appointments = models.ManyToManyField('Doctor', through='MedicalAppointment', related_name='person')
    meals = models.ManyToManyField(Meal, blank=True)
    prescribed_medicine = models.ManyToManyField(Prescription, blank=True)
    medicine = models.ManyToManyField(ConsumedMedicine, blank=True)

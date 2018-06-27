from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


# User profile, connected to an actual user in the system
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Usuário")
    cpf = models.CharField(max_length=11, blank=False, verbose_name="CPF")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Data de nascimento")


class Allergy(models.Model):
    name = models.CharField(max_length=100, blank=False, verbose_name="Nome")
    description = models.TextField(max_length=500, blank=True, verbose_name="Descrição")
    symptoms = models.TextField(max_length=500, blank=True, verbose_name="Sintomas")

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=100, blank=False, verbose_name="Nome")
    specialty = models.CharField(max_length=50, blank=False, verbose_name="Especialidade")

    def __str__(self):
        return self.name + ' - ' + self.specialty


class MedicalAppointment(models.Model):
    person = models.ForeignKey('Elderly', related_name='appointment', on_delete=models.CASCADE, verbose_name="Idoso")
    doctor = models.ForeignKey(Doctor, related_name='appointment', on_delete=models.CASCADE, verbose_name="Médico")
    description = models.TextField(max_length=500, blank=True, verbose_name="Descrição da consulta")
    date = models.DateTimeField(null=False, blank=False, verbose_name="Data/Hora")


class Food(models.Model):
    name = models.CharField(max_length=100, blank=False, verbose_name="Nome")

    def __str__(self):
        return self.name


class Meal(models.Model):
    MEAL_CHOICES = (
        ('CM', "Café da Manhã"),
        ('LA', "Lanche"),
        ('AL', "Almoço"),
        ('JA', "Janta"),
        ('CE', "Ceia")
    )
    type = models.CharField(max_length=30)
    meal_type = models.CharField(null=False, blank=False, max_length=2, choices=MEAL_CHOICES, verbose_name="Tipo de refeição")
    date = models.DateTimeField(null=False, blank=False, verbose_name="Data/Hora")
    foods = models.ManyToManyField(Food, blank=True, verbose_name="Alimentos")


class Medicine(models.Model):
    name = models.CharField(max_length=100, blank=False, verbose_name="Nome")
    description = models.TextField(max_length=500, blank=True, null=True, verbose_name="Descrição")

    def __str__(self):
        return self.name


class Prescription(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, verbose_name="Medicamento")
    startDate = models.DateField(blank=False, null=False, verbose_name="Data de início")
    endDate = models.DateField(blank=True, null=True, verbose_name="Data de fim")
    frequency = models.PositiveIntegerField(verbose_name="Frequência (horas)")  # In hours


class ConsumedMedicine(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, verbose_name="Medicamento")
    amount = models.PositiveIntegerField(blank=False, null=False, verbose_name="Dose")
    date = models.DateTimeField(blank=False, null=False, verbose_name="Data/Hora")


class Elderly(models.Model):
    name = models.CharField(max_length=100, blank=False, verbose_name="Nome")
    cpf = models.CharField(max_length=11, blank=False, verbose_name="CPF")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Data de nascimento")
    caretaker = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Cuidador")
    allergies = models.ManyToManyField(Allergy, blank=True, verbose_name="Alergias")
    medical_appointments = models.ManyToManyField('Doctor', through='MedicalAppointment', related_name='person', verbose_name="Consultas médicas")
    meals = models.ManyToManyField(Meal, blank=True, verbose_name="Refeições")
    prescribed_medicine = models.ManyToManyField(Prescription, blank=True, verbose_name="Medicamentos prescritos")
    medicine = models.ManyToManyField(ConsumedMedicine, blank=True, verbose_name="Medicamentos injeridos")

    def __str__(self):
        return self.name

    def get_age(self):
        return datetime.now().year - self.birth_date.year

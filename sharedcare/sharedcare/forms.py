from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Allergy, Doctor, Medicine, Elderly, Food, MedicalAppointment, Meal, Prescription, ConsumedMedicine


class AllergyForm(forms.ModelForm):
    class Meta:
        model = Allergy
        fields = ('name', 'description', 'symptoms',)


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('name', 'specialty',)


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ('name',)


class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ('name', 'description',)


class ElderlyForm(forms.ModelForm):
    class Meta:
        model = Elderly
        fields = ('name', 'cpf', 'birth_date',)


class ElderlyAllergyForm(forms.Form):
    allergies = forms.ModelChoiceField(queryset=Allergy.objects.all())


class ElderlyMedicalAppointmentForm(forms.ModelForm):
    class Meta:
        model = MedicalAppointment
        fields = ('date', 'doctor', 'description',)


class ElderlyMealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ('date', 'meal_type', 'foods',)


class ElderlyPrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ('medicine', 'startDate', 'endDate', 'frequency',)


class ElderlyConsumedMedicineForm(forms.ModelForm):
    class Meta:
        model = ConsumedMedicine
        fields = ('date', 'medicine', 'amount',)


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Nome.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Sobrenome.')
    email = forms.EmailField(max_length=254, required = True, help_text='Informe um email válido.')
    birth_date = forms.DateField(help_text='Formato: DD/MM/YYYY')
    cpf = forms.CharField(max_length=11, required=True, help_text="Informe seu CPF sem pontos ou traços.")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

from django import forms

from .models import Allergy, Doctor, Medicine, Elderly


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
        model = Doctor
        fields = ('name',)


class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ('name','description',)


class ElderlyForm(forms.ModelForm):
    class Meta:
        model = Elderly
        fields = ('name','cpf','birth_date',)


class ElderlyAllergyForm(forms.ModelForm):
    class Meta:
        model = Elderly
        fields = ('allergies',)
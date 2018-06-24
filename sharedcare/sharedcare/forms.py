from django import forms

from .models import Allergy, Doctor


class AllergyForm(forms.ModelForm):
    class Meta:
        model = Allergy
        fields = ('name', 'description', 'symptoms')


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('name', 'specialty')


class FoodForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('name',)
from django import forms

from .models import Allergy, Doctor, Medicine


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


class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ('name','description')
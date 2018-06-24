from django import forms

from .models import Allergy


class AllergyForm(forms.ModelForm):
    class Meta:
        model = Allergy
        fields = ('name', 'description', 'symptoms', )

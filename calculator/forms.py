# calculator/forms.py
from django import forms
from .models import GeneralTechnicalScore, SpecialTechnicalScore

class GeneralTechnicalForm(forms.ModelForm):
    class Meta:
        model = GeneralTechnicalScore
        fields = ['license_score', 'attendance_score', 'interview_score', 'additional_score']

class SpecialTechnicalForm(forms.ModelForm):
    class Meta:
        model = SpecialTechnicalScore
        fields = ['license_score', 'major_score', 'attendance_score', 'interview_score', 'additional_score']

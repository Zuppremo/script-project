from .models import CategoryGroup, Script
from django import forms

class CategoryGroupForm(forms.ModelForm):
    class Meta:
        model = CategoryGroup
        fields = ['name']

class ScriptForm(forms.ModelForm):
    class Meta:
        model = Script
        fields = ['CategoryGroup', 'name', 'content']
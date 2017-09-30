from django import forms
from .models import Tag


class InsertTag(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['tag']
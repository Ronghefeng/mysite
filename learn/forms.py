from django import forms
from .models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ("description", "document")


class AddForm(forms.Form):
    numb1 = forms.IntegerField()
    numb2 = forms.IntegerField()

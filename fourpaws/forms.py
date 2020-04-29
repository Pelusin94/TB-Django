from django import forms
from . import models

class FulfilmentInputForm(forms.Form):
    csv_file = forms.FileField()


class FulfilmentOutputForm(forms.Form):
    date_from = forms.CharField(widget=forms.DateInput(attrs={'type': 'date'}))
    date_to = forms.CharField(widget=forms.DateInput(attrs={'type': 'date'}))


class FulfilmentLettersUploadForm(forms.ModelForm):
    class Meta:
        model = models.UploadedFiles
        fields = ('file_name', 'file_path')

class FulfilmentLetterSelectForm(forms.Form):
    model = models.UploadedFiles.objects.all()
    letter_choices = [ (letter.file_path ,letter.file_name) for letter in model]
    letter = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=letter_choices)









from django import forms
from . import models
import csv


# forms------------------------------------------------------------------------------------------


class UploadedCsvFiles_form(forms.ModelForm):
    file_path = forms.FileField()
    class Meta:
        model = models.UploadedCsvFiles_table
        fields = ('file_path',)

    def clean_file_path(self):
        csv_file = self.cleaned_data['file_path']

        if not csv_file.name.endswith('.csv'):
            raise forms.ValidationError('This is not a CSV file')
        data = csv_file.read().decode('UTF-8').splitlines()
        dic_data = csv.DictReader(data)
        for row in dic_data:
            if row['charity_urn'] == '':
                raise forms.ValidationError('missing first column')
        csv_file.seek(0)
        return self.cleaned_data['file_path']



class UploadedWordFiles_form(forms.ModelForm):
    class Meta:
        model = models.UploadedWordFiles_table
        fields = ('file_description', 'file_path')


class FulfilmentOutputForm(forms.Form):
    date_from = forms.CharField(widget=forms.DateInput(attrs={'type': 'date'}))
    date_to = forms.CharField(widget=forms.DateInput(attrs={'type': 'date'}))


class FulfilmentLetterSelectForm(forms.Form):
    model = models.UploadedWordFiles_table.objects.all()
    letter_choices = [(letter.file_path, letter.file_description) for letter in model]
    letter = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=letter_choices)




from django import forms

class UploadForm(forms.Form):

    upload = forms.CharField()
    time = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
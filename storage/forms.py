from django import forms

class UploadForm(forms.Form):

    upload = forms.CharField()
    time = forms.IntegerField()
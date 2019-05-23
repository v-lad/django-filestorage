from django import forms

class UploadForm(forms.Form):
    """
    Form for uploading file. upload field is CharField, because files
    will be encoded in Base64 string format when form submits. 
    FileField waits file in request.FILES, so form couldn`t validates
    while the server will be handling it. On server Base64 string 
    decodes back to file.
    """
    upload = forms.CharField()
    time = forms.IntegerField()
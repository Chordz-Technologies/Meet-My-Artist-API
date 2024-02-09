# forms.py
from django import forms

class ImageUploadForm(forms.Form):
    image1 = forms.CharField(widget=forms.Textarea)
    image2 = forms.CharField(widget=forms.Textarea)
    image3 = forms.CharField(widget=forms.Textarea)
    image4 = forms.CharField(widget=forms.Textarea)
    image5 = forms.CharField(widget=forms.Textarea)

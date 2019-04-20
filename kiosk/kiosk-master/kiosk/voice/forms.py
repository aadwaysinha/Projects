from django import forms

class SpeechForm(forms.Form):
    data = forms.CharField(widget=forms.Textarea, label='')

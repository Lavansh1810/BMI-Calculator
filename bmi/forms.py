from django import forms

class NameForm(forms.Form):
    weight = forms.IntegerField()
    feet = forms.IntegerField()
    inch = forms.IntegerField()
    gender = forms.CharField()
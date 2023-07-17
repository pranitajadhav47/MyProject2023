from django import forms
from .models import blogcontain

class TestFromClass(forms.Form):
    name=forms.CharField(max_length=100)
    roll_no=forms.IntegerField()
    school_name=forms.CharField(max_length=100)

class ModelsDemoForm(forms.ModelForm):
    class Meta:
        model=blogcontain

        fields=['title','description','author','no_of_line','img']
from django import forms

def validate_for_a(svalue):
    if svalue[0]=='a':
        raise forms.ValidationError('name should not starts with a')

def validate_for_len(name):
    if len(name)<=9:
        raise forms.ValidationError('len is less than 9')




class StudentForm(forms.Form):
    sname=forms.CharField(max_length=100,validators=[validate_for_a,validate_for_len])
    sage=forms.IntegerField()
    email=forms.EmailField(validators=[validate_for_a])

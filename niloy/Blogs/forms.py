from django import forms
from django.core import validators

class TeachersRegistration(forms.Form):
    first_name=forms.CharField(label="Enter your First Name",label_suffix=' ')
    last_name=forms.CharField(initial="studymart")
    email=forms.EmailField(initial="niloy8649@gmail.com",disabled=True)
    password=forms.CharField(widget=forms.PasswordInput)
    repassword=forms.CharField(widget=forms.PasswordInput)
    textarea=forms.CharField(widget=forms.Textarea)
    file=forms.CharField(widget=forms.FileInput)
    checkbox=forms.CharField(widget=forms.CheckboxInput)



    def clean(self):
        cleaned_data=super().clean()
        rightpassword=self.cleaned_data['password']
        wrongpassword=self.cleaned_data['repassword']
        if rightpassword != wrongpassword:
            raise forms.ValidationError("password does not match")
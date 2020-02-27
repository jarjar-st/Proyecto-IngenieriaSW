from django import forms
from .models import Account

class AccountForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ['password','email','first_name','last_name','phone_number','address','birth_date']
        widgets={
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'phone_number':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'birth_date':forms.DateTimeInput(attrs={'type':'date','class':'form-control'}),
        }
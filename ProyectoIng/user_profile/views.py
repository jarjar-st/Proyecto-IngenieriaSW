from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from account.models import Account


# Create your views here.
class AccountUpdate(UpdateView):
    model = Account
    fields= ["email","first_name","last_name","birth_date", "phone_number","address","profile_img"]
    template_name_suffix = '_update_form'
   

    def get_success_url(self):
        return reverse_lazy('home')

    
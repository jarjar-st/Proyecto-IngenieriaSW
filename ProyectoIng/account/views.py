from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from account.models import Account
from .forms import AccountForm

# Create your views here.
class CreateUser(CreateView): #Pass,Correo,Nombre,Apellido,Telefono,Direccion,FechaN
    model = Account
    form_class=AccountForm
    success_url= reverse_lazy('login')
    template_name= 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login')+'?register'

class TemplateLogin(TemplateView):
    template_name= 'account/login.html'



    
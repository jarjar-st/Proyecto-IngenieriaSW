from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from account.models import Account
from .forms import AccountForm

# Create your views here.
class CreateUser(CreateView): #Pass,Correo,Nombre,Apellido,Telefono,Direccion,FechaN
    model = Account
    form_class=AccountForm
    
    success_url= reverse_lazy('test')
    template_name= 'registration/signup.html'



    
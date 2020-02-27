from django.shortcuts import redirect, render#Metodos de direccionamiento
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView #Objeto para la creacion de usuario, vista basada en Clase
from django.views.generic.base import TemplateView #Visualizacion de Template , Vista basada en Clase
from account.models import Account #Modelo de Usuario
from account.forms import RegistrationForm #Formulario de registro de usuario
from django.contrib.auth import logout  #Permite finalizar Sesion

# Create your views here.
class CreateUser(CreateView): #Pass,Correo,Nombre,Apellido,Telefono,Direccion,FechaN
    model = Account
    form_class=RegistrationForm
    template_name= 'registration/signup.html' #Template al que envia el formulario

    def get_success_url(self):
        return reverse_lazy('login')+'?register'

class TemplateLogin(TemplateView):#Visualizar Login
    template_name= 'account/login.html'

def logout_view(request):#Cerrar Sesion
    logout(request)
    return redirect('login')


    
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import DateField, DateInput, FloatField, ModelForm
from app_admon.models import *

class DateInput(forms.DateInput):
    input_type = 'Date'

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
             visible.field.widget.attrs['class'] = 'form-control'
             visible.field.widget.attrs['placeholder'] = visible.field.label

class Agregar_clienteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(Agregar_clienteForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

        self.fields['telefono'].widget.attrs.update(
            {'maxlength': '7', 'minlength': '7',
             'onkeypress': "return soloNumeros(event)"
             })
        self.fields['ced_rif'].widget.attrs.update(
            {'maxlength': '9'})
        self.fields['direccion'].widget.attrs['rows'] = 3
    #     self.fields['nacimiento'].widget.attrs.update(
    #         {'style': 'width: 340px'})
         
    ced_rif = forms.CharField(widget=forms.TextInput(attrs={'style': 'border-left: 0px;border-radius: 0px 25px 25px 0px'}))
    telefono = forms.CharField(widget=forms.TextInput(attrs={'style': 'border-left: 0px;border-radius: 0px 25px 25px 0px'}))
    nacimiento = forms.DateField(widget=DateInput)
      
    
    # nacimiento = forms.DateField(widget=forms.DateInput(attrs={'style': 'width: 305px'}))
       
    class Meta:
        model = Cliente
        fields = ('ced_rif','nombre', 'telefono', 'instagram', 'direccion', 'nacimiento', 'status')
        # widgets = {
        #      'nacimiento': DateInput(format=('%Y-%m-%d'))
         #  }

    
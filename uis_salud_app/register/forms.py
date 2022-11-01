from django import forms
from .models import Registropaciente


class RegistroPacienteFormGlucosa(forms.ModelForm):

    class Meta:

        model = Registropaciente

        fields = [
            'glucosa',   
        ]

        widgets = {
            'glucosa': forms.NumberInput(attrs={'class':'form-control data-imput','required':'','value':100,'min':20,'max':500}),            
        }

class RegistroPacienteFormPresion(forms.ModelForm):

    class Meta:

        model = Registropaciente

        fields = [
            'presionarterialdiastolica',
            'presionarterialsistolica',
        ]

        widgets = {
            'presionarterialdiastolica': forms.NumberInput(attrs={'class':'form-control data-imput','required':'','value':80, 'min':40,'max':150}),
            'presionarterialsistolica': forms.NumberInput(attrs={'class':'form-control data-imput','required':'','value':120, 'min':40,'max':250}),
        }


class RegistroPacienteMedidas(forms.ModelForm):

    class Meta:

        model = Registropaciente

        fields = [
            'peso',
            'perimetro_abdominal',
            'perimetro_pantorrilla',
        ]

        widgets = {
            'peso': forms.NumberInput(attrs={'class':'form-control data-imput','required':'','value':80}),
            'perimetro_abdominal': forms.NumberInput(attrs={'class':'form-control data-imput','required':'','value':80}),
            'perimetro_pantorrilla': forms.NumberInput(attrs={'class':'form-control data-imput','required':'','value':30}),
        }
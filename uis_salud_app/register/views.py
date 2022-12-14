from re import template
from django.shortcuts import render
from django.template import loader
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Registropaciente, Usuario
from .forms import RegistroPacienteFormGlucosa, RegistroPacienteFormPresion, RegistroPacienteMedidas

users = {"2022_1":1,"2022_2":2,"2022_3":3,"2022_4":4,"2022_5":5}

# Create your views here.
def login(request):
    template = loader.get_template('ingreso.html')
    if request.method == "POST":
        user = request.POST['user']
        user_db = Usuario.objects.filter(codigo=user)
        if len(user_db)==1:            
            request.session['user'] = user_db[0].id
        return redirect('home')  
    context = {}
    return HttpResponse(template.render(context,request))

def home(request):
    template = loader.get_template('index.html')
    user = request.session.get('user',None)
    if not user:
        return redirect('login') 
    context = {"user":user}
    return HttpResponse(template.render(context,request))

def glucosa(request):
    form = RegistroPacienteFormGlucosa(request.POST or None)
    if form.is_valid():
        comida = request.POST['comida']
        instance = form.save(commit=False)
        
        if comida == '1':
            #ayunas
            instance.despues_comida = 0            
        elif comida == '2':
            #2 horas despues de comer
            instance.despues_comida = 1
        elif comida == '3':
            #toma espontanea
            instance.despues_comida = 3
        
        #Obtener usuario de las cookies
        user = request.session.get('user',None)
        if user:
            instance.paciente = user
        instance.save()
        
        #ADVERTENCIAS 
        if instance.glucosa > 70 and instance.glucosa <180:
                messages.add_message(request, messages.INFO, 'Datos enviados correctamente, sus niveles de glucosa son normales. ¬°Felicidades!')
        elif instance.glucosa >180:
                return redirect('hiperglucemia')
        elif instance.glucosa < 70:
            return redirect('advertencia',id_advertencia=2)

        
        return redirect('home')    
    context = {"form":form}
    return render(request,"glucosa.html",context)


def tension_arterial(request):
    form = RegistroPacienteFormPresion(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        user = request.session.get('user',None)
        if user:
            instance.paciente = user
        instance.save()
        
        #ADVERTENCIAS 
        if instance.presionarterialsistolica < 180 and instance.presionarterialdiastolica <110:
            messages.add_message(request, messages.INFO, 'Datos enviados correctamente, sus niveles de presi√≥n en la sangre son normales. ¬°Felicidades!')
        elif instance.presionarterialsistolica < 200 and instance.presionarterialdiastolica <120:
            return redirect('advertencia',id_advertencia=1)
        else:
            return redirect('crisis_hiper')
        #Obtener usuario de las cookies
        
        return redirect('home')    
    context = {"form":form}
    return render(request,"arterial.html",context)


def medidas_corporales(request):
    form = RegistroPacienteMedidas(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)        
        #Obtener usuario de las cookies
        user = request.session.get('user',None)
        if user:
            instance.paciente = user
        instance.save()
        messages.add_message(request, messages.INFO, 'Datos enviados correctamente.')
        return redirect('home')
    ultima_medida = Registropaciente.objects.exclude(peso=None).order_by('fecharegistro');
    if len(ultima_medida)>0:
        registro = ultima_medida[len(ultima_medida)-1]
    else:
        registro = None
    context = {"form":form,"registro":registro}
    return render(request,"medidas.html",context)


def advertencia(request,id_advertencia):
    context = {"alerta":id_advertencia}
    return render(request,"advertencia.html",context)

def crisis_hiper(request):
    context = {}
    return render(request,"crisis_hiper.html",context)

def hiperglucemia(request):
    context = {}
    return render(request,"hiperglucemia.html",context)

def coma_diabetico(request):
    context = {}
    return render(request,"crisis_diabetes.html",context)

def hipoglucemia(request):
    context = {}
    return render(request,"hipoglucemia.html",context)

def no_crisis(request):
    context = {}
    return render(request,"no_crisis.html",context)



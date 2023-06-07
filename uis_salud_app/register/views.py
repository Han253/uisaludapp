import datetime
from pytz import timezone
from django.shortcuts import render
from django.template import loader
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Registropaciente, Usuario
from .forms import RegistroPacienteFormGlucosa, RegistroPacienteFormPresion, RegistroPacienteMedidas

def login(request):
    template = loader.get_template('ingreso.html')
    if request.method == "POST":
        user = request.POST['user']
        user_db = Usuario.objects.filter(codigo=user)
        if len(user_db)==1:            
            request.session['user'] = user_db[0].id
            request.session['user_name'] = user_db[0].primernombre + " " + user_db[0].primerapellido
        return redirect('home')  
    context = {}
    return HttpResponse(template.render(context,request))

def home(request):
    template = loader.get_template('index.html')
    user = request.session.get('user',None)
    user_name = request.session.get('user_name',None)
    if not user or not user_name:
        return redirect('login')
    else:
        resultado = Usuario.objects.filter(id=user)        
        if len(resultado) ==1:
            tz = timezone('America/Bogota')
            today = tz.localize(datetime.datetime.now())
            usuario = resultado[0]
            usuario.ultimoingreso = today
            usuario.save()
            registros = Registropaciente.objects.filter(paciente=user).order_by('-fecharegistro')
            if len(registros)>0:
                ultimo_registro = registros[0]
                dias = today-ultimo_registro.fecharegistro
                if dias > datetime.timedelta(days=2) :
                    messages.add_message(request, messages.INFO, 'Último registro enviado hace más de dos días, se recomienda ser constante en la toma de datos para un correcto monitoreo.')
        else:
            return redirect('login')

    context = {"user_name":user_name}
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
            instance.despues_comida = 2
        
        #Obtener usuario de las cookies
        user = request.session.get('user',None)
        if user:
            instance.paciente = user
        instance.save()
        
        #ADVERTENCIAS 
        if instance.glucosa > 70 and instance.glucosa <180:
                messages.add_message(request, messages.INFO, 'Datos enviados correctamente, sus niveles de glucosa son normales. ¡Felicidades!')
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
            messages.add_message(request, messages.INFO, 'Datos enviados correctamente, sus niveles de presión en la sangre son normales. ¡Felicidades!')
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
    context = {"form":form}
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

def informacion(request):
    context = {}
    return render(request,"informacion.html",context)

def indHistorial(request):
    context = {}
    return render(request,"ind_historial.html",context)

def histPresionArterial(request):
    #Obtener usuario de las cookies
    user = request.session.get('user',None)
    if user!=None:
        ultima_medida = Registropaciente.objects.filter(paciente=user).exclude(presionarterialsistolica=None).order_by('-fecharegistro');
        if len(ultima_medida)>0:
            registros = ultima_medida[:10]
        else:
            registros = None
        context={'registros':registros}
    else:
        context={'registros':None}
    return render(request,"historial_presion_arterial.html",context)

def histGlucosa(request):
    #Obtener usuario de las cookies
    user = request.session.get('user',None)
    if user!=None:
        ultima_medida = Registropaciente.objects.filter(paciente=user).exclude(glucosa=None).order_by('-fecharegistro');
        if len(ultima_medida)>0:
            registros = ultima_medida[:10]
        else:
            registros = None
        context={'registros':registros}
    else:
        context={'registros':None}
    return render(request,"historial_glucosa.html",context)

def histCorporal(request):
    #Obtener usuario de las cookies
    user = request.session.get('user',None)
    if user!=None:
        ultima_medida = Registropaciente.objects.filter(paciente=user).exclude(peso=None).order_by('-fecharegistro');
        if len(ultima_medida)>0:
            registros = ultima_medida[:10]
        else:
            registros = None
        context={'registros':registros}
    else:
        context={'registros':None}
    return render(request,"historial_medidas.html",context)





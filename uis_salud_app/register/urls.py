from django.urls import path, re_path

from . import views

sufix = 'uisaludapp'

urlpatterns = [
    path(sufix+'/',views.home, name='home'),
    path(sufix+'/login',views.login, name='login'),
    path(sufix+'/glucosa',views.glucosa, name='glucosa'),
    path(sufix+'/arterial',views.tension_arterial, name='arterial'),
    path(sufix+'/medidas',views.medidas_corporales, name='medidas'),
    path(sufix+'/advertencia/<id_advertencia>',views.advertencia, name='advertencia'),
    path(sufix+'/crisis/hipertensiva',views.crisis_hiper, name='crisis_hiper'),
    path(sufix+'/crisis/hiperglucemia', views.hiperglucemia, name='hiperglucemia'),
    path(sufix+'/crisis/coma_diabetico', views.coma_diabetico, name='coma_diabetico'),
    path(sufix+'/crisis/hipoglucemia', views.hipoglucemia, name='hipoglucemia'),
    path(sufix+'/no_crisis',views.no_crisis, name='no_crisis'),
    path(sufix+'/informacion',views.informacion, name='informacion')
]

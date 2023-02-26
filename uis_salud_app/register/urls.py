from django.urls import path, re_path

from . import views

urlpatterns = [
    path('uisalud/',views.home, name='home'),
    path('uisalud/login',views.login, name='login'),
    path('uisalud/glucosa',views.glucosa, name='glucosa'),
    path('uisalud/arterial',views.tension_arterial, name='arterial'),
    path('uisalud/medidas',views.medidas_corporales, name='medidas'),
    path('uisalud/advertencia/<id_advertencia>',views.advertencia, name='advertencia'),
    path('uisalud/crisis/hipertensiva',views.crisis_hiper, name='crisis_hiper'),
    path('uisalud/crisis/hiperglucemia', views.hiperglucemia, name='hiperglucemia'),
    path('uisalud/crisis/coma_diabetico', views.coma_diabetico, name='coma_diabetico'),
    path('uisalud/crisis/hipoglucemia', views.hipoglucemia, name='hipoglucemia'),
    path('uisalud/no_crisis',views.no_crisis, name='no_crisis'),
    path('uisalud/informacion',views.informacion, name='informacion')
]

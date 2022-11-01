from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('login',views.login, name='login'),
    path('glucosa',views.glucosa, name='glucosa'),
    path('arterial',views.tension_arterial, name='arterial'),
    path('medidas',views.medidas_corporales, name='medidas'),
    path('advertencia/<id_advertencia>',views.advertencia, name='advertencia'),
    path('crisis/hipertensiva',views.crisis_hiper, name='crisis_hiper'),
    path('crisis/hiperglucemia', views.hiperglucemia, name='hiperglucemia'),
    path('crisis/coma_diabetico', views.coma_diabetico, name='coma_diabetico'),
    path('crisis/hipoglucemia', views.hipoglucemia, name='hipoglucemia'),
    path('no_crisis',views.no_crisis, name='no_crisis')
]
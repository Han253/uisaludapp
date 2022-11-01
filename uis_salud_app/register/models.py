from django.db import models

# Create your models here.
class Registropaciente(models.Model):
    id = models.BigAutoField(primary_key=True)
    fecharegistro = models.DateTimeField(auto_now=True)
    glucosa = models.FloatField(blank=True, null=True)
    despues_comida = models.IntegerField(blank=True, null=True)
    perimetro_abdominal = models.FloatField(blank=True, null=True)
    perimetro_pantorrilla = models.FloatField(blank=True, null=True)
    peso = models.FloatField(blank=True, null=True)
    presionarterialdiastolica = models.IntegerField(blank=True, null=True)
    presionarterialsistolica = models.IntegerField(blank=True, null=True)
    paciente = models.BigIntegerField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'registropaciente'

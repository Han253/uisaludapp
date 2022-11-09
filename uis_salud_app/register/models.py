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
        managed = False
        db_table = 'registropaciente'

class Usuario(models.Model):
    id = models.BigIntegerField(primary_key=True)
    activo = models.TextField(blank=True, null=True)
    contrasena = models.CharField(max_length=255)
    correopersonal = models.CharField(max_length=255)
    descripcionpersonal = models.TextField(blank=True, null=True)
    fechaimagen = models.DateTimeField(blank=True, null=True)
    genero = models.IntegerField()
    imagenperfil = models.TextField(blank=True, null=True)
    movilwhatsapp = models.CharField(max_length=255, blank=True, null=True)
    nombre = models.CharField(max_length=255)
    primerapellido = models.CharField(max_length=255)
    primernombre = models.CharField(max_length=255)
    segundoapellido = models.CharField(max_length=255, blank=True, null=True)
    segundonombre = models.CharField(max_length=255, blank=True, null=True)
    tokenresetcontrasena = models.CharField(max_length=255, blank=True, null=True)
    tipo_usuario = models.CharField(max_length=31)
    fechanacimiento = models.DateField(blank=True, null=True)
    codigo = models.CharField(max_length=255, blank=True, null=True)
    diagnostico = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usuario'

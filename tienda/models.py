from django.db import models

from django.utils.text import slugify

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    escudo = models.ImageField(upload_to='equipos/', null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre



class Camiseta(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    jugador = models.CharField(max_length=100)
    numero = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)  
    foto_frente = models.ImageField(upload_to='camisetas/', null=True, blank=True)
    foto_espalda = models.ImageField(upload_to='camisetas/', null=True, blank=True)

    def __str__(self):
        return f"{self.jugador} - {self.equipo} ({self.numero})"



class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

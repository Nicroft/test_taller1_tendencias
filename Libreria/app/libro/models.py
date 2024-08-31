from django.db import models

class Libro(models.Model):
    ESTADO_CHOICES = [
        ('Disponible', 'Disponible'),
        ('Prestado', 'Prestado'),
    ]
    
    título = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    fecha_publicación = models.DateField()
    género = models.CharField(max_length=100)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES)

    def __str__(self):
        return self.título
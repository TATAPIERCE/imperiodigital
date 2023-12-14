from django.db import models

class Cita(models.Model):
    opciones_consultas = [
    [0, "Reparacion"],
    [1, "mantencion"],
    [2, "instalacion"]
]

    servicio = models.IntegerField(choices=opciones_consultas)
    nombre_del_cliente = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    celular = models.CharField(max_length=9)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    descripcion = models.TextField()



    def __str__(self):
        return f'{self.servicio} - {self.nombre_del_cliente} {self.direccion} - {self.fecha} {self.celular} {self.hora_inicio}'
    

    

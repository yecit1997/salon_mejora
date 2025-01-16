# from django.contrib.auth.models import User
# from django.db import models


# class Roles(models.Model):
#     nombre = models.CharField(max_length=30, unique=True)
    
#     def __str__(self):
#         return self.nombre
    

# # Create your models here.
# class Usuarios(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     dni = models.CharField(max_length=10, unique=True, primary_key=True)
#     telefono = models.CharField(max_length=20, unique=True)
#     rol = models.ManyToManyField(Roles)
#     fecha_creacion = models.DateTimeField(auto_now_add=True)
#     fecha_modificacion = models.DateTimeField(auto_now=True)
    
#     class Meta:
#         verbose_name = "usuario"
#         verbose_name_plural = "usuarios"
#         ordering = ["-fecha_creacion"]

#     def __str__(self):
#         return f'{self.user.first_name} {self.user.last_name}'
    




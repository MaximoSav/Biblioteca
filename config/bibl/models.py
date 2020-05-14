from django.db import models

# Create your models here.

class Autor(models.Model):
	nombre = models.CharField(max_length = 50)
	codigo = models.IntegerField(primary_key=True)
	
	def __str__(self):
		return ("{}:{}".format(self.nombre, self.codigo))

class Libro (models.Model):
	titulo = models.CharField(max_length = 50)
	editorial = models.CharField(max_length = 50)
	cant_pag = models.IntegerField()
	codigo = models.IntegerField(primary_key=True)
	codAutor = models.ForeignKey(Autor, on_delete=models.CASCADE, null = True)
	
	def __str__(self):
		return ("{}:{}".format(self.titulo, self.codAutor))

class Ejemplar (models.Model):
	localizacion = models.CharField(max_length = 50, null = True) 
	codigo = models.IntegerField(primary_key=True)
	codLibro = models.ForeignKey(Libro, on_delete=models.CASCADE, null = True)

	def __str__(self):
		return ("{}:{}".format(self.localizacion, self.codLibro))

class Usuarios (models.Model):
	nombre = models.CharField(max_length = 50)
	codigo = models.IntegerField(primary_key=True)
	telefono = models.IntegerField()
	direccion = models.CharField(max_length = 50, null = True)

	def __str__(self):
		return ("{}:{}".format(self.nombre, self.codigo))
		

	






from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from django.db import connection
from thumbs import ImageWithThumbsField

# Create your models here.
class usuario(models.Model):
	Nick=models.CharField(max_length=100)
	Email=models.EmailField(max_length=100)
	Password=models.CharField(max_length=20)

	def __unicode__(self):
		return "%s "%(self.Nick)
class Perfil(models.Model):	
	user=models.OneToOneField(User,unique=True)
	#pais=models.CharField(max_length="30", null=False)
	avatar=ImageWithThumbsField(upload_to="img_user",sizes=((50,50),(200,200)))
	puntaje_total=models.PositiveIntegerField(default=0)
 	partidas_jugadas=models.PositiveIntegerField(default=0)

class Tema(models.Model):
	nombre=models.CharField(max_length=20,unique=True)
	def __str__(self):
		return self.nombre

class Pregunta(models.Model):
	nombre=models.CharField(max_length=500)
	tema=models.ForeignKey(Tema)
	def __str__(self):
		return self.nombre


class Respuesta(models.Model):
	respuesta_correcta=models.CharField(max_length=500)
	respuesta_opcional=models.CharField(max_length=500)
	respuesta_opcional_1=models.CharField(max_length=500)
	respuesta_opcional_2=models.CharField(max_length=500)
	pregunta=models.ForeignKey(Pregunta)
	def __str__(self):
		return self.pregunta


class partida(models.Model):
	tipos=(('public','Publico'),('private','Privado'))
	cant_preguntas=(('10','10'),('20','20'),('30','30'),('40','40'),('50','50'))
	tiempo=(('10','10'),('15','15'),('20','20'),('25','25'),('30','30'),('35','35'),('40','40'),('45','45'),('50','50'),('55','55'),('60','60'))
	titulo=models.CharField(max_length=200)
	jugadores=models.PositiveIntegerField()
	tipo_partida=models.CharField(max_length=200,choices=tipos)
	preguntas=models.CharField(max_length=5, choices=cant_preguntas)
	tiempo_respuesta=models.CharField(max_length=5,choices=tiempo)
	categorias=models.ManyToManyField(Tema, blank=False)
	usuario=models.ForeignKey(User)
	def __unicode__(self):
		return self.titulo
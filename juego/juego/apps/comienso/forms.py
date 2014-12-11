#encoding:utf-8
from django import forms
from django.forms import ModelForm
from .models import *
import pdb
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import ReCaptchaField
from django.forms.extras.widgets import *
tipos=(('public','Publico'),('private','Privado'))
cant_preguntas=(('10','10'),('20','20'),('30','30'),('40','40'),('50','50'))
tiempo=(('10 segundos','10 segundos'),('15 segundos','15 segundos'),('20 segundos','20 segundos'),('25 segundos','25 segundos'),('30 segundos','30 segundos'),('35 segundos','35 segundos'),('40 segundos','40 segundos'),('45 segundos','45 segundos'),('50 segundos','50 segundos'),('55 segundos','55 segundos'),('60 segundos','60 segundos'))
categoria=Tema.objects.all()

class fcapcha(forms.Form):
	captcha = ReCaptchaField(attrs={'theme' : 'clean'})
class usuarioform(ModelForm):
 	class Meta:
 		model=usuario
class fperfil(ModelForm):
	class Meta:
		model=Perfil
		exclude=['user']
class fusuario(UserCreationForm):
	username=forms.CharField(max_length=40,required=True,help_text=False,label="Nick")
	password2=forms.CharField(help_text=False,label="Contraseña de confirmación", widget=forms.PasswordInput)
	#first_name=forms.CharField(max_length=50,required=True,label="Nombre")
	#last_name=forms.CharField(max_length=50,required=True,label="Apellido")
	email=forms.EmailField(max_length=100,required=True,label="Email")
	class Meta:
		model=User
		#fields=("username","password1","password2","first_name","last_name","email")
		fields=("username","password1","password2","email")
	def save(self, commit=True):
		user=super(fusuario,self).save(commit=False)
		#user.first_name=self.cleaned_data.get("first_name")
		#user.last_name=self.cleaned_data.get("last_name")
		user.email=self.cleaned_data.get("email")
		if commit:
			user.save()
		return user 
class fperfil_modificar(ModelForm):
	class Meta:
		model=Perfil
		exclude=['user']

class feditar_perfil(forms.Form):
	email=forms.EmailField(max_length=100,required=True,label="Email")
	#password=forms.CharField(help_text=False,label="Contraseña nueva", widget=forms.PasswordInput)
class feditar_pass(forms.Form):
	password=forms.CharField(help_text=False,label="Contraseña nueva", widget=forms.PasswordInput)




class ftema(ModelForm):
	class Meta:
		model=Tema
class fpregunta(ModelForm):
	nombre=forms.CharField(required=True,label="Pregunta :")
	class Meta:
		model=Pregunta
		exclude=['tema']
class frespuesta(ModelForm):
	class Meta:
		model=Respuesta
		exclude=['pregunta']

class fpartida(ModelForm):
	tipo_partida=forms.ChoiceField(widget=forms.RadioSelect,choices=tipos)
	categorias=forms.ModelMultipleChoiceField(queryset=Tema.objects.all(),widget=forms.CheckboxSelectMultiple()) 
	class Meta:
		model=partida
		exclude=["usuario"]
from django import forms
from .models import ContactProfile


class ContactForm(forms.ModelForm):

	name = forms.CharField(max_length=100, required=True,
		widget=forms.TextInput(attrs={
			'placeholder': '*Mi nombre es..',
			'class': 'form-control'
			}))
	email = forms.EmailField(max_length=254, required=True, 
		widget=forms.TextInput(attrs={
			'placeholder': '*Mi email es.. (verificar que sea correcto)',
			'class': 'form-control'
			}))
	message = forms.CharField(max_length=1000, required=True, 
		widget=forms.Textarea(attrs={
			'placeholder': '*Necesito un trabajo de "x" para el "y" de "z"',
			'class': 'form-control',
			'rows': 6,
			}))


	class Meta:
		model = ContactProfile
		fields = ('name', 'email', 'message',)
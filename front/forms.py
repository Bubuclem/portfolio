from django import forms
from django.forms import ModelForm, EmailInput, TextInput, Textarea
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible

from .models import Newsletter, Message

INPUT_CLASS = 'py-3 px-4 block w-full shadow-sm text-warm-gray-900 focus:ring-rose-500 focus:border-rose-500 border-warm-gray-300 rounded-md'
TEXTAREA_CLASS = 'py-3 px-4 block w-full shadow-sm text-warm-gray-900 focus:ring-rose-500 focus:border-rose-500 border border-warm-gray-300 rounded-md'
EMAIL_CLASS = 'block w-full border border-transparent rounded-md px-5 py-3 text-base text-gray-900 placeholder-gray-500 shadow-sm focus:outline-none focus:border-transparent focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-rose-500'

''' Form for contact '''
class contactForm(ModelForm):
    class Meta:
        model = Message
        fields = ['first_name', 'last_name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'first_name': TextInput(attrs={'class': INPUT_CLASS}),
            'last_name': TextInput(attrs={'class': INPUT_CLASS}),
            'email': EmailInput(attrs={'class': INPUT_CLASS}),
            'phone': TextInput(attrs={'class': INPUT_CLASS}),
            'subject': TextInput(attrs={'class': INPUT_CLASS}),
            'message': Textarea(attrs={'class': TEXTAREA_CLASS}),
        }

''' Form for newsletter '''
class newsletterForm(ModelForm):
    class Meta :
        model = Newsletter
        fields = ['email']
        labels = {'email': 'Courriel'}
        widgets = {
            'email': EmailInput(attrs={'class': EMAIL_CLASS, 'placeholder': 'Entrer votre courriel'})
        }

''' Google reCAPTCHA V2 - invisible '''
class reCAPTCHAV2Form(forms.Form):
    captcha = ReCaptchaField(widget=ReCaptchaV2Invisible)
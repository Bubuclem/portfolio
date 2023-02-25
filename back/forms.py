'''
Back app forms
'''
from django import forms
from django.forms import ModelForm

from back.models import User

CLASS_INPUT = ('appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm '
'placeholder-gray-400 focus:outline-none focus:ring-red-500 focus:border-red-500 sm:text-sm')
CLASS_BOOL = 'h-4 w-4 text-red-600 focus:ring-red-500 border-gray-300 rounded'
CLASS_FILE = ('ml-5 bg-white py-2 px-3 border border-gray-300 rounded-md shadow-sm text-sm '
'leading-4 font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 '
'focus:ring-offset-2 focus:ring-red-500')
CLASS_CHECKBOX = 'focus:ring-red-500 h-4 w-4 text-red-600 border-gray-300 rounded'

class LoginForm(forms.Form):
    '''
    Login form
    '''
    email = forms.EmailField(label='Email',
    widget=forms.TextInput(attrs={'class': CLASS_INPUT}))
    password = forms.CharField(label='Password',
    widget=forms.PasswordInput(attrs={'class': CLASS_INPUT}))
    remember_me = forms.BooleanField(label='Remember me',
    required=False, widget=forms.CheckboxInput(attrs={'class': CLASS_BOOL}))

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        if not email or not password:
            raise forms.ValidationError('Please fill in all fields.')
        return cleaned_data

class ProfilForm(ModelForm):
    '''
    Profil form
    '''
    class Meta:
        '''
        Meta class for ProfilForm
        '''
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'picture_profile']
        widgets = {
            'username': forms.TextInput(attrs={'class': CLASS_INPUT}),
            'first_name': forms.TextInput(attrs={'class': CLASS_INPUT}),
            'last_name': forms.TextInput(attrs={'class': CLASS_INPUT}),
            'email': forms.TextInput(attrs={'class': CLASS_INPUT}),
            'picture_profile': forms.FileInput(attrs={'class': CLASS_FILE}),
        }

class UserForm(ModelForm):
    '''
    User form
    '''
    class Meta:
        '''
        Meta class for UserForm
        '''
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'picture_profile', 'is_active',
        'is_staff', 'is_superuser']
        widgets = {
            'username': forms.TextInput(attrs={'class': CLASS_INPUT}),
            'first_name': forms.TextInput(attrs={'class': CLASS_INPUT}),
            'last_name': forms.TextInput(attrs={'class': CLASS_INPUT}),
            'email': forms.TextInput(attrs={'class': CLASS_INPUT}),
            'picture_profile': forms.FileInput(attrs={'class': CLASS_FILE}),
            'is_active': forms.CheckboxInput(attrs={'class': CLASS_CHECKBOX}),
            'is_staff': forms.CheckboxInput(attrs={'class': CLASS_CHECKBOX}),
            'is_superuser': forms.CheckboxInput(attrs={'class': CLASS_CHECKBOX}),
        }

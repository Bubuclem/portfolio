from django import forms

CLASS_INPUT = 'appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-red-500 focus:border-red-500 sm:text-sm'
CLASS_BOOL = 'h-4 w-4 text-red-600 focus:ring-red-500 border-gray-300 rounded'

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': CLASS_INPUT}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': CLASS_INPUT}))
    remember_me = forms.BooleanField(label='Remember me', required=False, widget=forms.CheckboxInput(attrs={'class': CLASS_BOOL}))

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        if not email or not password:
            raise forms.ValidationError('Please fill in all fields.')
        return cleaned_data
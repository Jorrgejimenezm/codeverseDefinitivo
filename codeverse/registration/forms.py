from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class FormularioRegistroConCorreo(UserCreationForm):
    email = forms.EmailField(
        required=True,
        help_text='Obligatorio, máximo 30 caracteres y válido',
        widget=forms.EmailInput(attrs={'placeholder': 'Correo electrónico'})
    )
    user_level = forms.ChoiceField(
        choices=UserProfile.USER_LEVEL_CHOICES,
        label='Nivel de usuario',
        widget=forms.Select(attrs={'placeholder': 'Selecciona el nivel de usuario'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'user_level')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Contraseña'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Repetir contraseña'}),
        }

    def clean_email(self):
        correo = self.cleaned_data.get('email')
        if User.objects.filter(email=correo).exists():
            raise forms.ValidationError("El correo ya está registrado.")
        return correo

    def save(self, commit=True):
        user = super(FormularioRegistroConCorreo, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            user_profile = UserProfile.objects.create(user=user, user_level=self.cleaned_data['user_level'])
        return user

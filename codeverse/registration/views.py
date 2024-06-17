from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import FormularioRegistroConCorreo

class Registro(CreateView):
    form_class = FormularioRegistroConCorreo
    template_name = 'registration/registro.html'
    
    def get_success_url(self) -> str:
        return reverse_lazy('login') + "?registroOk"
    
    def get_form(self, form_class=None):
        form = super(Registro, self).get_form(form_class)
        for fieldname in ['username', 'email', 'password1', 'password2']:
            form.fields[fieldname].widget.attrs.update({'class': 'form-control mb-2'})
            form.fields[fieldname].label = ""
        return form

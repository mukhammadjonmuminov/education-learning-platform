from django import forms
from django.forms.models import inlineformset_factory
from .models import Courses, Modul

ModuleFormSet = inlineformset_factory(Courses, Modul, fields=['title', 'description'], extra=2, can_delete=True)

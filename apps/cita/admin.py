from django.contrib import admin
from .models import Cita
from django.forms import TimeInput
from django.db import models

class CitaAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TimeField: {'widget': TimeInput(attrs={'type': 'time'})},
    }

admin.site.register(Cita, CitaAdmin)

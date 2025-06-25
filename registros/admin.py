from django.contrib import admin
from .models import Alumnos

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
# Register your models here.
admin.site.register(Alumnos, AdministrarModelo)
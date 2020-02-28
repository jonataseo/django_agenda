from django.contrib import admin
from core.models import Evento

# Register your models here.

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data_evento', 'data_criacao')
    list_filter = ('titulo',)
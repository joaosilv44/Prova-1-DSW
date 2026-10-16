from django.contrib import admin
from .models import Modalidade, Equipe, Tecnico, Atleta

class ModalidadeAdmin(admin.ModelAdmin):
    pass

class AtletaInline(admin.TabularInline):
    list_display = ["nome", "matricula", "equipe"]
    list_filter = ["equipe", "modalidade"]
    

admin.site.register(Modalidade)
admin.site.register(Equipe)
admin.site.register(Tecnico)
admin.site.register(Atleta)
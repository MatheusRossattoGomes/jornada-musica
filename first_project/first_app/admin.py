from django.contrib import admin
from .models import Empresa, BandaArtista, Contrato, Evento, BandaArtistaArquivo, BandaArtistaInstrumentos, Instrumento, BandaArtistaGeneroDeApresentacao, Usuario
# Register your models here.

admin.site.register(Empresa)
admin.site.register(BandaArtista)
admin.site.register(Contrato)
admin.site.register(Evento)
admin.site.register(BandaArtistaArquivo)
admin.site.register(BandaArtistaInstrumentos)
admin.site.register(Instrumento)
admin.site.register(BandaArtistaGeneroDeApresentacao)

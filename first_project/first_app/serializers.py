from rest_framework import serializers 
from first_app.models import Instrumento, ResultadoMineracao, Cupom, BandaArtista, Empresa, Evento, Contrato
 
 
class InstrumentoSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Instrumento
        fields = ('id',
                  'nome',
                  'idTipoInstrumento')
 
class ResultadoMineracaoSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = ResultadoMineracao
        fields = ('id',
                  'maiorTendencia',
                  'menorTendencia',
                  'valorDataHora')
 
class CupomSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Cupom
        fields = ('id',
                  'porcentagem',
                  'generoMusical',
                  'valorDataHora')                  
 
class EmpresaSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Empresa
        fields = ('id',
                  'nome',
                  'email',
                  'idTipoUsuario',
                  'cnpj')                  
 
class BandaArtistaSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = BandaArtista
        fields = ('id',
                  'nome',
                  'email',
                  'idTipoUsuario',
                  'numeroIntegrantes',
                  'cpfOuCnpj',
                  'valorDataHora')

class EventoSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Evento
        fields = ('id',
                  'idStatus',
                  'idEmpresa',
                  'idPorteEvento',
                  'duracao',
                  'data',
                  'nome',
                  'local')

class ContratoSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Contrato
        fields = ('id',
                  'idStatus',
                  'idEvento',
                  'idEmpresa',
                  'idBandaArtista',
                  'valorTotal',
                  'empresaAceitou',
                  'bandaArtistaAceitou')


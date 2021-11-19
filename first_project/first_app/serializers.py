from rest_framework import serializers 
from first_app.models import Instrumento, ResultadoMineracao, Cupom, BandaArtista, Empresa, Evento, Contrato, BandaArtistaGeneroDeApresentacao, BandaArtistaInstrumentos
 
 
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
                  
class BandaArtistaGeneroDeApresentacaoSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = BandaArtistaGeneroDeApresentacao
        fields = ('id',
                  'idGeneroMusical')         

class BandaArtistaInstrumentosSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = BandaArtistaInstrumentos
        fields = ('id',
                  'idInstrumento')
 
class BandaArtistaSerializer(serializers.ModelSerializer):
    
    generos = BandaArtistaGeneroDeApresentacaoSerializer(many=True)
    instrumentos = BandaArtistaInstrumentosSerializer(many=True)

    class Meta:
        model = BandaArtista
        fields = ('id',
                  'nome',
                  'email',
                  'idTipoUsuario',
                  'numeroIntegrantes',
                  'cpfOuCnpj',
                  'valorDataHora',
                  'generos',
                  'instrumentos')
    
    def create(self, validated_data):
        generos = validated_data.pop("generos")
        instrumentos = validated_data.pop("instrumentos")
        banda_artista = BandaArtista.objects.create(**validated_data)
        for genero in generos:
            teste = BandaArtistaGeneroDeApresentacao.objects.create(idBandaArtista = banda_artista, **genero)
            banda_artista.generos =  teste
        for instrumento in instrumentos:
            teste = BandaArtistaInstrumentos.objects.create(idBandaArtista = banda_artista, **instrumento)
            banda_artista.instrumentos =  teste
        return banda_artista

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



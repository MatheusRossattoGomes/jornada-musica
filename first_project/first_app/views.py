from django.db.models.query import Prefetch
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from first_app.models import BandaArtistaInstrumentos, Instrumento, ResultadoMineracao, BandaArtista, Evento, BandaArtistaGeneroDeApresentacao
from first_app.serializers import ResultadoMineracaoSerializer, EmpresaSerializer, CupomSerializer, BandaArtistaSerializer, EventoSerializer, ContratoSerializer, InstrumentoSerializer, BandaArtistaGeneroDeApresentacaoSerializer, BandaArtistaInstrumentosSerializer
from rest_framework.decorators import api_view
from first_app.mineracao import coletarDadosTweets
import datetime
from first_app.generosMusicaisEnum import generosMusicais



@api_view(['GET'])
def get_instrumentos(request):
        if request.method == 'GET':
            instrumentos =  Instrumento.objects.all()
            instrumento_serializer = InstrumentoSerializer(instrumentos, many=True)
        return JsonResponse(instrumento_serializer.data, safe=False)

        
@api_view(['GET'])
def gerar_dados_tweets(request):
        if request.method == 'GET':
            resultados = coletarDadosTweets()
            dados_resultado_mineracao = {}
            dados_resultado_mineracao['maiorTendencia'] = int(resultados[0])  
            dados_resultado_mineracao['menorTendencia'] = int(resultados[1]) 
            dados_resultado_mineracao['valorDataHora'] = datetime.datetime.now()            
            resultado_mineracao_serializer = ResultadoMineracaoSerializer(data=dados_resultado_mineracao)
            if resultado_mineracao_serializer.is_valid():
                resultado_mineracao_serializer.save()
                return JsonResponse(resultado_mineracao_serializer.data, status=status.HTTP_200_OK) 
            return JsonResponse(resultado_mineracao_serializer.errors, status=status.HTTP_400_BAD_REQUEST)        
                
@api_view(['GET'])
def gerar_cupoms(request):
        if request.method == 'GET':
            data = datetime.date.today()
            resultadosMineracao = list(ResultadoMineracao.objects.filter(valorDataHora__gte=data))


            qtdMaiorTendenciaSertanejo = len([e for e in resultadosMineracao if e.maiorTendencia == int(generosMusicais.Sertanejo)])
            qtdMaiorTendenciaRock = len([e for e in resultadosMineracao if e.maiorTendencia == int(generosMusicais.Rock)])
            qtdMaiorTendenciaSamba = len([e for e in resultadosMineracao if e.maiorTendencia == int(generosMusicais.Samba)])
            qtdMaiorTendenciaPagode = len([e for e in resultadosMineracao if e.maiorTendencia == int(generosMusicais.Pagode)])
            qtdMaiorTendenciaFunk = len([e for e in resultadosMineracao if e.maiorTendencia == int(generosMusicais.Funk)])

            
            listaQtdGeneroMaisFalado = [qtdMaiorTendenciaSertanejo, qtdMaiorTendenciaRock, qtdMaiorTendenciaSamba, qtdMaiorTendenciaPagode, qtdMaiorTendenciaFunk]         
            generoMaisFaladoQtd = max(listaQtdGeneroMaisFalado)
            generoMaisFalado = None

            if(generoMaisFaladoQtd == qtdMaiorTendenciaSertanejo):
                generoMaisFalado = generosMusicais.Sertanejo
            elif(generoMaisFaladoQtd == qtdMaiorTendenciaRock):
                generoMaisFalado = generosMusicais.Rock
            elif(generoMaisFaladoQtd == qtdMaiorTendenciaSamba):
                generoMaisFalado = generosMusicais.Samba
            elif(generoMaisFaladoQtd == qtdMaiorTendenciaPagode):
                generoMaisFalado = generosMusicais.Pagode
            elif(generoMaisFaladoQtd == qtdMaiorTendenciaFunk):
                generoMaisFalado = generosMusicais.Funk

            qtdMenorTendenciaSertanejo = len([e for e in resultadosMineracao if e.menorTendencia == int(generosMusicais.Sertanejo)])
            qtdMenorTendenciaRock = len([e for e in resultadosMineracao if e.menorTendencia == int(generosMusicais.Rock)])
            qtdMenorTendenciaSamba = len([e for e in resultadosMineracao if e.menorTendencia == int(generosMusicais.Samba)])
            qtdMenorTendenciaPagode = len([e for e in resultadosMineracao if e.menorTendencia == int(generosMusicais.Pagode)])
            qtdMenorTendenciaFunk = len([e for e in resultadosMineracao if e.menorTendencia == int(generosMusicais.Funk)])

            
            listaQtdGeneroMenosFalado = [qtdMenorTendenciaSertanejo, qtdMenorTendenciaRock, qtdMenorTendenciaSamba, qtdMenorTendenciaPagode, qtdMenorTendenciaFunk]
            generoMenosFaladoQtd = max(listaQtdGeneroMenosFalado)
            generoMenosFalado = None

            if(generoMenosFaladoQtd == qtdMenorTendenciaSertanejo):
                generoMenosFalado = generosMusicais.Sertanejo
            elif(generoMenosFaladoQtd == qtdMenorTendenciaRock):
                generoMenosFalado = generosMusicais.Rock
            elif(generoMenosFaladoQtd == qtdMenorTendenciaSamba):
                generoMenosFalado = generosMusicais.Samba
            elif(generoMenosFaladoQtd == qtdMenorTendenciaPagode):
                generoMenosFalado = generosMusicais.Pagode
            elif(generoMenosFaladoQtd == qtdMenorTendenciaFunk):
                generoMenosFalado = generosMusicais.Funk
                     
            cupomMaisFalado = {}   
            cupomMaisFalado['porcentagem'] = 5 
            cupomMaisFalado['generoMusical'] = int(generoMaisFalado)
            cupomMaisFalado['valorDataHora'] = datetime.datetime.now()  
            cupomMenosFalado = {}
            cupomMenosFalado['porcentagem'] = 10 
            cupomMenosFalado['generoMusical'] = int(generoMenosFalado)
            cupomMenosFalado['valorDataHora'] = datetime.datetime.now()  

            cupomMaisFaladoSerializado = CupomSerializer(data=cupomMaisFalado)
            cupomMenosFaladoSerializado = CupomSerializer(data=cupomMenosFalado); 
            if cupomMaisFaladoSerializado.is_valid():
                cupomMaisFaladoSerializado.save()
            else: return JsonResponse(cupomMaisFaladoSerializado.errors, status=status.HTTP_400_BAD_REQUEST)
            if cupomMenosFaladoSerializado.is_valid():
                cupomMenosFaladoSerializado.save()
            else: return JsonResponse(cupomMenosFaladoSerializado.errors, status=status.HTTP_400_BAD_REQUEST)
            
            resultado = {}
            resultado['cupomGeneroMaisFalado'] = cupomMaisFaladoSerializado.data
            resultado['cupomGeneroMenosFalado'] = cupomMenosFaladoSerializado.data
            return JsonResponse(resultado, status=status.HTTP_201_CREATED) 
            
@api_view(['POST'])
def add_usuario(request):
        if request.method == 'POST':
            dados = request.data

            if(dados['idTipoUsuario'] == -1): #BandaArtista
                return add_banda_artista(dados)
            elif(dados['idTipoUsuario'] == -2): #Empresa
                dados['cnpj'] = dados['cnpj'].replace('.','').replace('-','').replace('/','')
                empresa_serializer = EmpresaSerializer(data=dados)
                if empresa_serializer.is_valid():
                    empresa_serializer.save()
                    return JsonResponse(empresa_serializer.data, status=status.HTTP_201_CREATED) 
                return JsonResponse(empresa_serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

def add_banda_artista(dados): 
    dados['cpfOuCnpj'] = dados['cpfOuCnpj'].replace('.','').replace('-','').replace('/','')
    banda_artista_serializer = BandaArtistaSerializer(data=dados)
    if banda_artista_serializer.is_valid():
       banda_artista_serializer.save()   
       return JsonResponse({"resultado":"Adicionado com sucesso"}, status=status.HTTP_201_CREATED) 
    return JsonResponse(banda_artista_serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
 


@api_view(['POST'])
def add_evento(request):
        if request.method == 'POST':
            dados = request.data 
            dados['idStatus'] = -3 # 'Agendado'
            evento_serializer = EventoSerializer(data=dados)
            if evento_serializer.is_valid():
                evento_serializer.save()
                return JsonResponse(evento_serializer.data, status=status.HTTP_201_CREATED) 
            return JsonResponse(evento_serializer.errors, status=status.HTTP_400_BAD_REQUEST)                  

@api_view(['POST'])
def add_contrato(request):
        if request.method == 'POST':
            dados = request.data 

            valorDataHora = get_valor_hora_banda_artista(dados['idBandaArtista'])
            evento = get_evento(dados['idEvento']) 

            print(evento.idEmpresa.id)

            dados['valorTotal'] = round(valorDataHora * evento.duracao, 2)
            dados['empresaAceitou'] = True
            dados['bandaArtistaAceitou'] = False
            dados['idEmpresa'] = evento.idEmpresa
            dados['idStatus'] = -3 # 'Aguandando aprovação'

            contrato_serializer = ContratoSerializer(data=dados)
            if contrato_serializer.is_valid():
                contrato_serializer.save()
                return JsonResponse(contrato_serializer.data, status=status.HTTP_201_CREATED) 
            return JsonResponse(contrato_serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

def get_valor_hora_banda_artista(id_banda_artista):
            banda_artista = BandaArtista.objects.get(pk=id_banda_artista)
            return banda_artista.valorDataHora

def get_evento(id_evento):
            evento = Evento.objects.get(pk=id_evento)
            return evento            

@api_view(['GET'])
def get_banda_artista(request, pk):
            banda_artista = BandaArtista.objects.get(pk=pk)
            generos = BandaArtistaGeneroDeApresentacao.objects.filter(idBandaArtista = pk)
            instrumentos = BandaArtistaInstrumentos.objects.filter(idBandaArtista = pk)
            banda_artista.generos = generos
            banda_artista.instrumentos = instrumentos
            banda_arista_serealize = BandaArtistaSerializer(banda_artista)
            print(banda_arista_serealize.data)
            return JsonResponse(banda_arista_serealize.data, status=status.HTTP_200_OK) 

@api_view(['GET'])
def get_generos_banda_artista(request):
            generos = BandaArtistaGeneroDeApresentacao.generosDeApresentacao
            return JsonResponse(generos, status=status.HTTP_200_OK, safe =False) 


# @api_view(['POST'])
# def add_instrumento(request):
#         if request.method == 'POST':
#             instrumento_json = JSONParser().parse(request)
#             instrumento_serializer = InstrumentoSerializer(data=instrumento_json)
#             if instrumento_serializer.is_valid():
#                 instrumento_serializer.save()
#                 return JsonResponse(instrumento_serializer.data, status=status.HTTP_201_CREATED) 
#             return JsonResponse(instrumento_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
 
# @api_view(['GET', 'PUT', 'DELETE'])
# def first_apptutorial_detail(request, pk):
#     # find tutorial by pk (id)
#     try: 
#         tutorial = Instrumento.objects.get(pk=pk) 
#     except Instrumento.DoesNotExist: 
#         return JsonResponse({'message': 'The Instrumento does not exist'}, status=status.HTTP_404_NOT_FOUND) 
#     return None
#     # GET / PUT / DELETE tutorial
    
        
# @api_view(['GET'])
# def first_app_published(request):
#     # GET all published first_app
#     return None

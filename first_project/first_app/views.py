from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from first_app.models import Instrumento, ResultadoMineracao
from first_app.serializers import InstrumentoSerializer, ResultadoMineracaoSerializer, EmpresaSerializer, CupomSerializer, BandaArtistaSerializer
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
                return JsonResponse(resultado_mineracao_serializer.data, status=status.HTTP_201_CREATED) 
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

            dados ={}
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
                dados['cpfOuCnpj'] = dados['cpfOuCnpj'].replace('.','').replace('-','').replace('/','')
                banda_artista_serializer = BandaArtistaSerializer(data=dados)
                if banda_artista_serializer.is_valid():
                    banda_artista_serializer.save()
                    return JsonResponse(banda_artista_serializer.data, status=status.HTTP_201_CREATED) 
                return JsonResponse(banda_artista_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            elif(dados['idTipoUsuario'] == -2): #Empresa
                dados['cnpj'] = dados['cnpj'].replace('.','').replace('-','').replace('/','')
                empresa_serializer = EmpresaSerializer(data=dados)
                if empresa_serializer.is_valid():
                    empresa_serializer.save()
                    return JsonResponse(empresa_serializer.data, status=status.HTTP_201_CREATED) 
                return JsonResponse(empresa_serializer.errors, status=status.HTTP_400_BAD_REQUEST)                
            


@api_view(['GET'])
def get_valores_Genero_enum(request):
        if request.method == 'GET':
            
            instrumento_json = JSONParser().parse(request)
            instrumento_serializer = InstrumentoSerializer(data=instrumento_json)
            if instrumento_serializer.is_valid():
                instrumento_serializer.save()
                return JsonResponse(instrumento_serializer.data, status=status.HTTP_201_CREATED) 
            return JsonResponse(instrumento_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

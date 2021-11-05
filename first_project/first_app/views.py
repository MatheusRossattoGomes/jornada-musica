from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from first_app.models import Instrumento
from first_app.serializers import InstrumentoSerializer
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_instrumentos(request):
        if request.method == 'GET':
            instrumentos =  Instrumento.objects.all()
            instrumento_serializer = InstrumentoSerializer(instrumentos, many=True)
        return JsonResponse(instrumento_serializer.data, safe=False)

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

from rest_framework import serializers 
from first_app.models import Instrumento
 
 
class InstrumentoSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Instrumento
        fields = ('id',
                  'nome',
                  'idTipoInstrumento')

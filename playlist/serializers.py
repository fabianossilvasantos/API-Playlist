from rest_framework import serializers
from .models import Album, Musica

class MusicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musica
        fields = ['id', 'titulo', 'artista', 'duracao_segundos', 'favorita', 'album']

class AlbumSerializer(serializers.ModelSerializer):
    musicas = MusicaSerializer(many=True, read_only=True)
    class Meta:
        model = Album
        fields = ['id', 'titulo', 'ano_lancamento', 'musicas']
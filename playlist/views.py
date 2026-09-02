from rest_framework import viewsets

from .models import Album, Musica
from .serializers import AlbumSerializer, MusicaSerializer

# viewset --> faz todo meu crud 
class MusicaViewSet(viewsets.ModelViewSet):
    queryset = Musica.objects.all()
    serializer_class = MusicaSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

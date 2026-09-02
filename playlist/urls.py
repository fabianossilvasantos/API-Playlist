from rest_framework.routers import DefaultRouter

from .views import  AlbumViewSet, MusicaViewSet 

router = DefaultRouter()

router.register(r'musicas', MusicaViewSet, basename='musica')
router.register(r'albuns', AlbumViewSet, basename='album')
urlpatterns = router.urls
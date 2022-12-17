from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from rest_framework.pagination import PageNumberPagination
from .serializers import SongSerializer
from albums.models import Album
from rest_framework.generics import ListCreateAPIView



class SongView(ListCreateAPIView, PageNumberPagination):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Song.objects.filter(album=self.kwargs['pk'])

    def perform_create(self, serializer):
        return serializer.save(album=Album.objects.get(pk=self.kwargs['pk']))

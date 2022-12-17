from rest_framework.views import APIView, status, Response
from .models import Album
from .serializers import AlbumSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import ListCreateAPIView


class AlbumView(ListCreateAPIView, PageNumberPagination):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        album = Album.objects.all()
        return album

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

from rest_framework import status, viewsets
from rest_framework.response import Response
from ..models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from .permissions import IsOwner,IsViewer



class BookViewSet(viewsets.ModelViewSet):
   
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(publisher=self.request.user)
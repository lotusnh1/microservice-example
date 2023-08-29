from rest_framework import serializers

from ..models import Book



class BookSerializer(serializers.ModelSerializer):

    publisher=serializers.PrimaryKeyRelatedField(read_only=True,required=False)
    class Meta:
        model = Book
        fields = ['title','description','author','book_img','publisher']
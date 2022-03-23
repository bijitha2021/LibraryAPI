from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from library.models import Book
from library.serializers import BookSerializer

# Create your views here.

class BookList(APIView):
    def get(self,request):
        books=Book.objects.all()
        bookserializer=BookSerializer(books,many=True)
        return Response(bookserializer.data)

    def post(self,request):
        book=request.data
        books=BookSerializer(data=book)
        if books.is_valid():
            books.save()
            return Response(books.data, status=status.HTTP_201_CREATED)
        else:
            return Response(books.data, status=status.HTTP_400_BAD_REQUEST)






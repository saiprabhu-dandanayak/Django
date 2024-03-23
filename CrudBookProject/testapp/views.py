from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import  Book
from .serializers import BookSerializer
from django.shortcuts import get_object_or_404

@api_view(['POST'])
def createBook(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def GetAllBooks(request):
    books=Book.objects.all()
    serializer=BookSerializer(books,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def GetBookById(request,pk):
    book=get_object_or_404(Book,pk=pk)
    serializer=BookSerializer(book)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def GetBookByTitle(request,title):
    book=Book.objects.filter(title__icontains=title)
    serializer = BookSerializer(book, many=True) 
    return Response(serializer.data)

@api_view(['PUT', 'PATCH'])
def update_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    serializer = BookSerializer(book, data=request.data, partial=True) 
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def DeleteBookById(request,pk):
    book=get_object_or_404(Book,pk=pk)
    book.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def DeleteBookByTitle(request, title):
    book=Book.objects.filter(title__icontains=title)
    book.delete()
    return  Response(status=status.HTTP_204_NO_CONTENT)

@api_view
def DeleteAllBooks(request):
    books=Book.objects.all()
    books.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
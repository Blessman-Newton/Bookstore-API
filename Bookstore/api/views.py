from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookSerializer, OrderSerializer, ReviewSerializer

# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.object.all()
    serializer_class = BookSerializer
    
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.object.all()
    serializer_class = OrderSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.object.all()
    serializer_class = ReviewSerializer
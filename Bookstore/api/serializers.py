from rest_framework import serializers
from .models import Book, Order, Review


class BookSerializer(serializers.Model):
    class Meta:
        db_table = ''
        managed = True
        model = Book
        field = '__all__'
        

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        field = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        field = '__all__'
        
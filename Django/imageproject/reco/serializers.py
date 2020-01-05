from .models import *
from rest_framework import serializers

class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = ['id','name', 'price','text','image']

class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ['name', 'age','species']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['feed', 'pub_date', 'user_name', 'comment' ,'rating']

class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ( 'url', 'items',)

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ( 'url', 'items','cart')
from django.shortcuts import render
from .models import Feed,Dog,Cart,Order,Tip,Review
from .serializers import FeedSerializer,DogSerializer,ReviewSerializer,CartSerializer,OrderSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from keras.models import load_model
from PIL import Image
import numpy as np
import tensorflow as tf
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
import random
from django.db.models import Avg,F
from django.core import serializers
import random
# Create your views here.

class FeedViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
class DogViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# model = load_model('resnet50_dog_model.h5')
# graph = tf.get_default_graph()

@csrf_exempt
def post(request):
    return HttpResponse('hi')

def tip(request):
    queryset = Tip.objects.all()
    ran = random.randrange(1,4)-1
    return JsonResponse({'tip':queryset[ran].text},json_dumps_params={'ensure_ascii': False}) 

@csrf_exempt
def ranking(request):
    avg_list = Feed.objects.filter(review__user_dog = request.POST['user_dog']).annotate(score = Avg('review__rating'))
    ranking_list = avg_list.order_by('-score')
    max_id = Feed.objects.order_by('-id')[0].id
    random_id = random.randint(1, max_id+1)
    random_object = Feed.objects.filter(id__gte=random_id)
    result = ranking_list | random_object
    for i in result:
        print(i,i.score)
    posts_serialized = serializers.serialize('json', result)
    return JsonResponse(posts_serialized, safe = False)
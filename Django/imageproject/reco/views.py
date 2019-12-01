from django.shortcuts import render
from .models import Feed,Dog,Cart,Order,Tip,Review,Shampoo,Snack
from .serializers import FeedSerializer,DogSerializer,ReviewSerializer,CartSerializer,OrderSerializer,ShampooSerializer,SnackSerializer
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
from rest_framework import status
# Create your views here.

class FeedViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
class ShampooViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Shampoo.objects.all()
    serializer_class = ShampooSerializer
class SnackViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer
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


model = load_model('model.h5')
graph = tf.get_default_graph()

@csrf_exempt
def post(request):
    global graph
    with graph.as_default():
        test_image = request.FILES['model_pic']
        img = Image.open(test_image)
        img = img.convert("RGB")
        img = img.resize((224,224))
        data = np.asarray(img)
        X = np.array(data)
        X = X.astype("float") / 256
        X = X.reshape(-1, 224, 224, 3)
        categories = ['GermanShepherd', 'GoldenRetriever', 'SiberianHusky']
        pred = model.predict(X)
        print(pred)
        result = [np.argmax(value) for value in pred]  
        print('New data category : ',categories[result[0]])
        return HttpResponse(categories[result[0]])

def tip(request):
    queryset = Tip.objects.all()
    ran = random.randrange(1,4)-1
    return HttpResponse(queryset[ran].text)

def feed(request):
    queryset = Feed.objects.all()
    return HttpResponse(queryset)

def shampoo(request):
    queryset = Shampoo.objects.all()
    return HttpResponse(queryset)

def snack(request):
    queryset = Snack.objects.all()
    return HttpResponse(queryset)

@csrf_exempt
def ranking(request):
    print(request.POST)
    avg_list = Feed.objects.filter(review__user_dog = request.POST['user_dog']).annotate(score = Avg('review__rating'))
    ranking_list = avg_list.order_by('-score')
    max_id = Feed.objects.order_by('-id')[0].id
    random_id = random.randint(1, max_id+1)
    random_object = Feed.objects.filter(id__gte=random_id)
    result = ranking_list | random_object
    for i in result:
        print(i,i.score)
    post_list = serializers.serialize('python',result,fields=('id','name','price','text','image'))
    actual_data = [d['fields'] for d in post_list]
    # and now dump to JSON
    output = json.dumps(actual_data)
    return HttpResponse(output, content_type="text/json-comment-filtered")

@csrf_exempt
def shampooranking(request):
    print(request.POST)
    # avg_list = Shampoo.objects.filter(review__user_dog = request.POST['user_dog']).annotate(score = Avg('review__rating'))
    # ranking_list = avg_list.order_by('-score')
    max_id = Shampoo.objects.order_by('-id')[0].id
    random_id = random.randint(1, max_id+1)
    random_object = Shampoo.objects.filter(id__gte=random_id)
    result = random_object
    # for i in result:
    #     print(i,i.score)
    post_list = serializers.serialize('python',result,fields=('id','name','price','text','image'))
    actual_data = [d['fields'] for d in post_list]
    # and now dump to JSON
    output = json.dumps(actual_data)
    return HttpResponse(output, content_type="text/json-comment-filtered")


@csrf_exempt
def snackranking(request):
    print(request.POST)
    # avg_list = Snack.objects.filter(review__user_dog = request.POST['user_dog']).annotate(score = Avg('review__rating'))
    # ranking_list = avg_list.order_by('-score')
    max_id = Snack.objects.order_by('-id')[0].id
    random_id = random.randint(1, max_id+1)
    random_object = Snack.objects.filter(id__gte=random_id)
    result =  random_object
    # for i in result:
    #     print(i,i.score)
    post_list = serializers.serialize('python',result,fields=('id','name','price','text','image'))
    actual_data = [d['fields'] for d in post_list]
    # and now dump to JSON
    output = json.dumps(actual_data)
    return HttpResponse(output, content_type="text/json-comment-filtered")
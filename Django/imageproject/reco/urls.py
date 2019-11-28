from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from django.conf.urls import include, url
from keras.models import load_model
router = DefaultRouter()
router.register('feed', views.FeedViewSet)
router.register('shampoo', views.ShampooViewSet)
router.register('snack', views.SnackViewSet)
router.register('dog', views.DogViewSet)
router.register('review', views.ReviewViewSet)
router.register('cart', views.CartViewSet)
router.register('order', views.OrderViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('pot/upload/',views.post),
    path('tip/',views.tip),
    path('ranking/',views.ranking),
    path('shampooranking/',views.shampooranking),
    path('snackranking/',views.snackranking),
    path('feed/',views.feed),
    path('shampoo/',views.shampoo),
    path('snack/',views.snack),
	]
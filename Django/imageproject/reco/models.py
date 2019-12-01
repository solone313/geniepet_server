from django.db import models
from django.contrib.auth import get_user_model
import numpy as np

User = get_user_model()
# Create your models here.
class Feed(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=30)
    text = models.CharField(max_length=1000)
    image = models.URLField()
    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name

class Shampoo(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=30)
    text = models.CharField(max_length=1000)
    image = models.URLField()
    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name

class Snack(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=30)
    text = models.CharField(max_length=1000)
    image = models.URLField()
    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name
    
class Dog(models.Model):
    #user foreignKey
    objects = models.Manager()
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    species = models.CharField(max_length=50)
    def __str__(self):
        return self.name+': '+self.species

 
class Review(models.Model):
    objects = models.Manager()
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    feed = models.ForeignKey(Feed,on_delete=models.CASCADE, related_name="review")
    pub_date = models.DateTimeField('date published')
    user_dog = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)


class Cart(models.Model):
    objects = models.Manager()
    status = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE, related_name="carts")
    items = models.ManyToManyField(Feed)    


class Order(models.Model):
    objects = models.Manager()
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE, blank=True, null=True)
    items = models.ManyToManyField(Feed) 
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE, related_name="orders")

class Tip(models.Model):    
    objects = models.Manager()
    text = models.CharField(max_length=1000, blank=True, null=True)
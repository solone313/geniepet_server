from django.contrib import admin
from .models import Feed,Cart,Order,Tip,Review
# Register your models here.
admin.site.register(Feed)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Tip)
admin.site.register(Review)
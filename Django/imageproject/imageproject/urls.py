
from django.contrib import admin
from django.urls import path

from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from reco.urls import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('image/', include('image_app.urls')),
    path('post/', include('create_app.urls')),
    path('blog/', include('blog.urls')),
    path('auth/',include('rest_auth.urls')),
    path('auth/register/',include('rest_auth.registration.urls')),
    path('', include('reco.urls')),
    path('', include('payment.urls')),
	]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path
from core.views import home
from core.views import categorias
from core.views import manifesto
from core.views import sobre

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path('categorias/', categorias, name='categorias'),
    path('manifesto/', manifesto, name='manifesto'),
    path('sobre/', sobre, name='sobre'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
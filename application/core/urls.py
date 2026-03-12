from django.contrib import admin
from django.urls import path
from . import views
from core.views import home, categorias, manifesto, sobre

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path('categorias/', categorias, name='categorias'),
    path('manifesto/', manifesto, name='manifesto'),
    path('sobre/', sobre, name='sobre'),
    path('conteudo/<slug:slug>/', views.conteudo_detail, name='conteudo_detail'),
    path('categoria/<slug:slug>/', views.categoria_detail, name='categoria_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
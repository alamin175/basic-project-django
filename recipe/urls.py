from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from django.conf import settings

from . import views

urlpatterns = [
    path('re/', views.recipe),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
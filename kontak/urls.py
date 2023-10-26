from . import views
from django.urls import path


urlpatterns = [
    path('kontak/', views.kontak_view, name='kontak')
]
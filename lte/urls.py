rom . import views
from django.urls import path


urlpatterns = [
    path('lte/', views.index, name='index')
]
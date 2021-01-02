from django.urls import path

from . import views 

urlpatterns = [
    path('', views.IndexView, name='list'),
    path('<cardcode>', views.CardView, name='card')
]
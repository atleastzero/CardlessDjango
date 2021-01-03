from django.urls import path

from . import views 

urlpatterns = [
    path('', views.IndexView.as_view(), name='list'),
    path('<slug:pk>/', views.CardView.as_view(), name='card')
]
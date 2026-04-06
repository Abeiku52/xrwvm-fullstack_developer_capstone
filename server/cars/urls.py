from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_car_makes_models, name='all-car-makes-models'),
    path('makes/', views.CarMakeListView.as_view(), name='car-makes'),
    path('djangoapp/get_cars/', views.get_cars, name='get-cars'),
]
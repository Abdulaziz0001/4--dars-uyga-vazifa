from django.urls import path
from .views import index, colors, brands, cars, add_cars

urlpatterns = [
    path('', index, name='home'),
    path('colors/<int:color_id>/', colors, name='colors'),
    path('brands/<int:brand_id>/', brands, name='brands'),
    path('cars/<int:car_id>/', cars, name='cars'),
    path('add_cars/', add_cars, name='add_cars')
]

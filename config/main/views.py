from http.client import HTTPResponse

from django.http import HttpRequest
from django.shortcuts import render, redirect
from .forms import CarsForm

from .models import Color, Brand, Car


# Create your views here.


def index(request):
    color = Color.objects.all()
    brand = Brand.objects.all()
    car = Car.objects.all()
    context = {
        "colors": color,
        "brands": brand,
        "cars": car
    }
    return render(request, "index.html", context)


def colors(request, color_id):
    color = Car.objects.filter(color_id=color_id)
    context = {
        "colors": color
    }
    return render(request, "index.html", context)


def brands(request, brand_id):
    brand = Car.objects.filter(brand_id=brand_id)
    context = {
        "brands": brand
    }
    return render(request, "index.html", context)


def cars(request, car_id):
    car = Car.objects.filter(id=car_id)
    context = {
        "cars": car
    }
    return render(request, "index.html", context)


def add_cars(request: HttpRequest):
    if request.method == "POST":
        form = CarsForm(data=request.POST)
        if form.is_valid():
            cars = Car.objects.create(**form.cleaned_data)
            print(cars)
            return redirect('cars', cars.pk)
    else:
        form = CarsForm()
    context = {
        "form": CarsForm()
    }
    return render(request, "add_cars.html", context)
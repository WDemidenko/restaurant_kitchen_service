from django.shortcuts import render
from django.views import generic

from kitchen.models import Dish, DishType, Cook


def index(request):
    num_cooks = Cook.objects.count()
    num_dishtypes = DishType.objects.count()
    num_dishes = Dish.objects.count()
    context = {
        "num_cooks": num_cooks,
        "num_dishtypes": num_dishtypes,
        "num_dishes": num_dishes,
    }

    return render(request, "kitchen/index.html", context=context)


class DishTypeListView(generic.ListView):
    model = DishType


class CookListView(generic.ListView):
    model = Cook


class DishListView(generic.ListView):
    model = Dish

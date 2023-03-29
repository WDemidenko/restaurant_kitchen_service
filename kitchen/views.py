from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kitchen.forms import DishTypeForm, DishForm, CookForm
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


class DishTypeDetailView(generic.DetailView):
    model = DishType

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dish_type = self.object
        dishes_count = dish_type.dishes.count()
        context["dishes_count"] = dishes_count
        return context


class DishTypeCreateView(SuccessMessageMixin, generic.CreateView):
    model = DishType
    form_class = DishTypeForm
    success_url = reverse_lazy("kitchen:dish-type-list")
    success_message = "%(name)s has been successfully created"


class DishTypeUpdateView(SuccessMessageMixin, generic.UpdateView):
    model = DishType
    form_class = DishTypeForm
    success_message = "%(name)s has been successfully updated"

    def get_success_url(self):
        dish_type_id = self.object.id
        return reverse_lazy('kitchen:dishtype-detail', kwargs={'pk': dish_type_id})


class DishTypeDeleteView(generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("kitchen:dish-type-list")


class CookListView(generic.ListView):
    model = Cook
    queryset = Cook.objects.prefetch_related("dishes")


class CookDetailView(generic.DetailView):
    model = Cook


class CookCreateView(generic.CreateView):
    model = Cook
    form_class = CookForm
    success_message = "%(username) has been successfully created"
    success_url = reverse_lazy("kitchen:cook-list")


class CookUpdateView(generic.UpdateView):
    model = Cook
    form_class = CookForm
    success_message = "%(username) has been successfully updated"

    def get_success_url(self):
        user_id = self.object.id
        return reverse_lazy('kitchen:cook-detail', kwargs={'pk': user_id})


class CookDeleteView(generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("kitchen:cook-list")


def assign_delete_cook_for_dish(request, pk):
    dish = Dish.objects.get(id=pk)
    cook = Cook.objects.get(id=request.user.id)
    if cook in dish.cooks.all():
        cook.dishes.remove(pk)
    else:
        cook.dishes.add(pk)

    return HttpResponseRedirect(reverse_lazy("kitchen:dish-detail", args=[pk]))


class DishListView(generic.ListView):
    model = Dish


class DishDetailView(generic.DetailView):
    model = Dish


class DishCreateView(SuccessMessageMixin, generic.CreateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("kitchen:dish-list")
    success_message = "%(name)s has been successfully created"


class DishUpdateView(SuccessMessageMixin, generic.UpdateView):
    model = Dish
    form_class = DishForm
    success_message = "%(name)s has been successfully updated"

    def get_success_url(self):
        dish_id = self.object.id
        return reverse_lazy('kitchen:dish-detail', kwargs={'pk': dish_id})


class DishDeleteView(generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen:dish-list")

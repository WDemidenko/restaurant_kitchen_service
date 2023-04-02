from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kitchen.forms import (
    DishTypeForm,
    DishForm,
    CookForm,
    DishTypeNameSearchForm,
    DishNameSearchForm,
    DishIngredientPickForm, CookUpdateForm
)
from kitchen.models import Dish, DishType, Cook, Ingredient


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


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishTypeListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = DishTypeNameSearchForm(
            initial={"name": name}
        )

        return context

    def get_queryset(self):
        queryset = DishType.objects.all()
        form = DishTypeNameSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])

        return queryset


class DishTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = DishType

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dish_type = self.object
        dishes_count = dish_type.dishes.count()
        context["dishes_count"] = dishes_count
        return context


class DishTypeCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = DishType
    form_class = DishTypeForm
    success_url = reverse_lazy("kitchen:dish-type-list")
    success_message = "%(name)s has been successfully created"


class DishTypeUpdateView(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = DishType
    form_class = DishTypeForm
    success_message = "%(name)s has been successfully updated"

    def get_success_url(self):
        dish_type_id = self.object.id
        return reverse_lazy("kitchen:dishtype-detail", kwargs={"pk": dish_type_id})


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("kitchen:dish-type-list")


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    queryset = Cook.objects.prefetch_related("dishes")
    paginate_by = 10


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    form_class = CookForm
    success_message = "%(username) has been successfully created"
    success_url = reverse_lazy("kitchen:cook-list")


class CookUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Cook
    form_class = CookUpdateForm
    success_message = "%(username) has been successfully updated"

    def get_success_url(self):
        user_id = self.object.id
        return reverse_lazy("kitchen:cook-detail", kwargs={"pk": user_id})

    def test_func(self):
        cook = self.get_object()
        return self.request.user.id == cook.id


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
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


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = DishNameSearchForm(
            initial={"name": name}
        )

        return context

    def get_queryset(self):
        queryset = Dish.objects.all()
        form = DishNameSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])

        return queryset


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish


class DishCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("kitchen:dish-list")
    success_message = "%(name)s has been successfully created"


class DishUpdateView(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = Dish
    form_class = DishForm
    success_message = "%(name)s has been successfully updated"

    def get_success_url(self):
        dish_id = self.object.id
        return reverse_lazy("kitchen:dish-detail", kwargs={"pk": dish_id})


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen:dish-list")


class IngredientListView(LoginRequiredMixin, SuccessMessageMixin, generic.ListView):
    model = Ingredient
    paginate_by = 10


class DishIngredientPickView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    form_class = DishIngredientPickForm
    template_name = "kitchen/take_ingredients.html"

    def get_success_url(self):
        dish_id = self.object.id
        return reverse_lazy("kitchen:dish-detail", kwargs={"pk": dish_id})

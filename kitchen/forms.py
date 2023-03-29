from django import forms
from django.contrib.auth.forms import UserCreationForm

from kitchen.models import DishType, Dish, Cook


class DishTypeForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = ["name"]


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = "__all__"


class CookForm(UserCreationForm):
    class Meta:
        model = Cook
        fields = ["username", "first_name", "last_name", "years_of_experience"]

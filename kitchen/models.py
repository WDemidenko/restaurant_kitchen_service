from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(
        validators=[MinValueValidator(0)]
    )

    class Meta:
        ordering = ["-years_of_experience"]


class DishType(models.Model):
    name = models.CharField(max_length=65, unique=True)

    class Meta:
        ordering = ["name"]


class Dish(models.Model):
    name = models.CharField(max_length=65, unique=True)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=10, decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    dish_type = models.ForeignKey(
        DishType,
        related_name="dishes",
        on_delete=models.SET_NULL,
        null=True
    )
    cooks = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="dishes")

    class Meta:
        verbose_name_plural = "dishes"


class Ingredient(models.Model):
    name = models.CharField(max_length=65, unique=True)

    class Meta:
        ordering = ["name"]

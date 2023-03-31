from _decimal import Decimal
from django.test import TestCase

from kitchen.forms import DishTypeNameSearchForm, DishNameSearchForm
from kitchen.models import DishType, Dish


class DishTypeListSearchTest(TestCase):
    def setUp(self):
        self.dishtype1 = DishType.objects.create(name="dishtype1")
        self.dishtype2 = DishType.objects.create(name="dishtype_second_test")
        self.dishtype3 = DishType.objects.create(name="dishtype_third_test")

    def test_search_dishtype_by_name(self):
        form_data = {"name": "test"}
        form = DishTypeNameSearchForm(form_data)
        self.assertTrue(form.is_valid())
        queryset = DishType.objects.filter(
            name__icontains=form.cleaned_data["name"]
        )
        self.assertEqual(queryset.count(), 2)
        self.assertNotIn(self.dishtype1, queryset)


class DishListSearchTest(TestCase):
    def setUp(self):
        self.dishtype = DishType.objects.create(name="dishtype1")
        self.dish1 = Dish.objects.create(
            name="dish",
            description="test_description1",
            price=Decimal("100"),
            dish_type=self.dishtype
        )
        self.dish2 = Dish.objects.create(
            name="DISH_some",
            description="test_description2",
            price=Decimal("100"),
            dish_type=self.dishtype
        )
        self.dish3 = Dish.objects.create(
            name="Some",
            description="test_description3",
            price=Decimal("100"),
            dish_type=self.dishtype
        )

    def test_search_dishtype_by_name(self):
        form_data = {"name": "some"}
        form = DishNameSearchForm(form_data)
        self.assertTrue(form.is_valid())
        queryset = Dish.objects.filter(
            name__icontains=form.cleaned_data["name"]
        )
        self.assertEqual(queryset.count(), 2)
        self.assertNotIn(self.dish1, queryset)

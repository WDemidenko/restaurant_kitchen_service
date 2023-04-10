from _decimal import Decimal
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import Dish, DishType


class AssignToDishTest(TestCase):
    def setUp(self) -> None:
        self.admin = get_user_model().objects.create(
            username="test",
            password="test1234",
            first_name="first",
            last_name="last"
        )
        self.dishtype = DishType.objects.create(name="test_dishtype")
        self.dish = Dish.objects.create(
            name="dish",
            description="test_description",
            price=Decimal("12"),
            dish_type=self.dishtype
        )
        self.client.force_login(self.admin)

    def test_assign_cook_for_dish(self):
        response = self.client.get(
            reverse("kitchen:assign_delete_cook", args=[self.dish.pk])
        )
        self.assertEqual(response.status_code, 302)
        self.assertIn(self.dish, self.admin.dishes.all())

    def test_delete_cook_from_dish(self):
        self.admin.dishes.add(self.dish)
        response = self.client.get(
            reverse("kitchen:assign_delete_cook", args=[self.dish.pk])
        )
        self.assertEqual(response.status_code, 302)
        self.assertNotIn(self.dish, self.admin.dishes.all())


class DishTypeRangeDishesTest(TestCase):
    def setUp(self) -> None:
        self.admin = get_user_model().objects.create(
            username="test",
            password="test1234",
            first_name="first",
            last_name="last"
        )
        self.dishtype = DishType.objects.create(name="dishtype")
        self.dish1 = Dish.objects.create(
            name="dish1",
            description="test_description1",
            price=Decimal("100"),
            dish_type=self.dishtype
        )
        self.dish2 = Dish.objects.create(
            name="dish2",
            description="test_description2",
            price=Decimal("100"),
            dish_type=self.dishtype
        )
        self.dish3 = Dish.objects.create(
            name="dish3",
            description="test_description3",
            price=Decimal("100"),
            dish_type=self.dishtype
        )
        self.client.force_login(self.admin)

    def test_dishtype_details_contains_correct_range_of_dishes(self):
        response = self.client.get(reverse("kitchen:dishtype-detail", args=[self.dishtype.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["dishes_count"], 3)


class CookChangeAnotherCookProfileTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create(
            username="test",
            password="test1234",
            first_name="first",
            last_name="last"
        )
        self.cook1 = get_user_model().objects.create(
            username="cook1",
            password="cook1_1234",
            first_name="first_cook1",
            last_name="last_cook1"
        )
        self.client.force_login(self.user)

    def test_user_changing_another_cook_account(self):
        user_page = self.client.get(reverse("kitchen:cook-update", args=[self.user.pk]))
        self.assertEqual(user_page.status_code, 200)
        cook_page = self.client.get(reverse("kitchen:cook-update", args=[self.cook1.pk]))
        self.assertEqual(cook_page.status_code, 403)

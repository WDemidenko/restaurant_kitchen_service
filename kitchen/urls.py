from django.urls import path

from kitchen.views import index, DishTypeListView, CookListView, DishListView, DishTypeDetailView, CookDetailView, \
    DishTypeCreateView, DishTypeUpdateView, DishTypeDeleteView, DishCreateView, DishUpdateView, DishDeleteView, \
    DishDetailView, CookCreateView, CookUpdateView, CookDeleteView, assign_delete_cook_for_dish, IngredientListView, \
    DishIngredientPickView

urlpatterns = [
    path("", index, name="index"),
    path(
        "dishtypes/",
        DishTypeListView.as_view(),
        name="dish-type-list"
    ),
    path(
        "dishtypes/<int:pk>/",
        DishTypeDetailView.as_view(),
        name="dishtype-detail"
    ),
    path(
        "cooks/",
        CookListView.as_view(),
        name="cook-list"
    ),
    path(
        "cooks/<int:pk>/",
        CookDetailView.as_view(),
        name="cook-detail"
    ),
    path(
        "dishes/",
        DishListView.as_view(),
        name="dish-list"
    ),
    path("dishtypes/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
    path("dishtypes/<int:pk>/update/", DishTypeUpdateView.as_view(), name="dish-type-update"),
    path("dishtypes/<int:pk>/delete/", DishTypeDeleteView.as_view(), name="dish-type-delete"),
    path(
        "dishes/create/",
        DishCreateView.as_view(),
        name="dish-create"
    ),
    path(
        "dishes/<int:pk>/update/",
        DishUpdateView.as_view(),
        name="dish-update"
    ),
    path(
        "dishes/<int:pk>/delete/",
        DishDeleteView.as_view(),
        name="dish-delete"
    ),
    path(
        "dishes/<int:pk>/",
        DishDetailView.as_view(),
        name="dish-detail"
    ),
    path("cooks/create/", CookCreateView.as_view(), name="cook-create"),
    path(
        "cooks/<int:pk>/update/",
        CookUpdateView.as_view(),
        name="cook-update"
    ),
    path(
        "cooks/<int:pk>/delete/",
        CookDeleteView.as_view(),
        name="cook-delete"
    ),
    path(
        "dishes/<int:pk>/assign_delete/",
        assign_delete_cook_for_dish,
        name="assign_delete_cook"
    ),
    path("ingredients/", IngredientListView.as_view(), name="ingredient-list"),
    path(
        "dishes/<int:pk>/take_ingredients/",
        DishIngredientPickView.as_view(),
        name="dish-take-ingredient"
    ),
]

app_name = "kitchen"

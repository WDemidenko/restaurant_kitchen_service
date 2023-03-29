from django.urls import path

from kitchen.views import index, DishTypeListView, CookListView, DishListView, DishTypeDetailView, CookDetailView, \
    DishTypeCreateView, DishTypeUpdateView, DishTypeDeleteView, DishCreateView, DishUpdateView, DishDeleteView

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
]

app_name = "kitchen"

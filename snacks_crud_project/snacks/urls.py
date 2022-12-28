from django.urls import path
from .views import (
    HomeView,
    SnackDetailView,
    SnackListView,
    SnackCreateView,
    SnackUpdateView,
    SnackDeleteView,
)

urlpatterns = [
    path("home/", HomeView.as_view(), name="snack_list"),
    path("", SnackListView.as_view(), name="snack_list"),
    path("<int:pk>/", SnackDetailView.as_view(), name="snack_detail"),
    path("create/", SnackCreateView.as_view(), name="snack_create"),
    path("update/<int:pk>/", SnackUpdateView.as_view(), name="snack_update"),
    path("delete/<int:pk>/", SnackDeleteView.as_view(), name="snack_delete"),
]

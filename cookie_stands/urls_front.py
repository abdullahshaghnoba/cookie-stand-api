from django.urls import path
from .views_front import (
    CookieStandCreateView,
    CookieStandDeleteView,
    CookieStandDetailView,
    CookieStandListView,
    CookieStandUpdateView,
)

urlpatterns = [
    path("", CookieStandListView.as_view(), name="CookieStand_list"),
    path("<int:pk>/", CookieStandDetailView.as_view(), name="CookieStand_detail"),
    path("create/", CookieStandCreateView.as_view(), name="CookieStand_create"),
    path('update/<int:pk>/', CookieStandUpdateView.as_view(), name='CookieStand_update'),
    path("delete/<int:pk>/", CookieStandDeleteView.as_view(), name="CookieStand_delete"),
]

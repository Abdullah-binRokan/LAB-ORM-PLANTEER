from django.urls import path
from . import views

app_name = "plants"

urlpatterns = [
    path("all/", views.plants_all_view, name = "plants_all_view"),
    path("new/", views.plants_new_view, name = "plants_new_view"),
    path("search/", views.plants_search_view, name = "plants_search_view"),
    path("<plant_id>/detail/", views.plants_detail_view, name = "plants_detail_view"),
    path("<plant_id>/update/", views.plants_update_view, name = "plants_update_view"),
    path("<plant_id>/delete/", views.plants_delete_view, name = "plants_delete_view"),
]

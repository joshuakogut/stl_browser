from django.urls import path
from stl_app import views

urlpatterns = [
    path("list/", views.list_stl_files, name="list_stl_files"),
    path("view/<str:filename>/", views.stl_viewer, name="stl_viewer"),
]

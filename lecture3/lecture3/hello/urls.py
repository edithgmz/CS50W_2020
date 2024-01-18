from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("edith", views.edith, name="edith"),
    path("malu", views.malu, name="malu")
]

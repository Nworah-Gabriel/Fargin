from django.urls import path
from . import views

urlpatterns = [

    # account urls
    path("", views.index, name="index"),
    path("coming-soon", views.soon, name="coming-soon"),
]
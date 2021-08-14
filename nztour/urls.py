from django.urls import path

from . import views

urlpatterns = [path("", views.index, name="index"),
               path("tours/<str:name>/", views.tours, name="tours")

]

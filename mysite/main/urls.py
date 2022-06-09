from django.urls import path

from . import views

# Reikia Auth middleware arba router blocking
urlpatterns = [
  path("<int:id>", views.index, name="index"),
  path("", views.home, name="home"),
  path("create/", views.create, name="create"),
  path("view/", views.view, name="view"),
]


from django.urls import path

from . import views

urlpatterns = [
    path("<int:id>", views.indexid, name='index'),
    path("<str:name>", views.index, name='index'),

    path("create/", views.create, name='create'),
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("view/", views.view, name="view")
]
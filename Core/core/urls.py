from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    # path('treeview', views.treeview),
    path('get_fs', views.get_fs)
]
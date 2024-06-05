from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index),
    path("futureExpen", views.futureExpen),
    path("history", views.history),
    path("addnote", views.addnote),
    path("addcoin", views.addcoin),
    path("addbank", views.addbank),
    path("addother", views.addother),
    path("withdrawnote", views.withdrawnote),
    path("withdrawcoin", views.withdrawcoin),
    path("withdrawbank", views.withdrawbank),
    path("withdrawother", views.withdrawother),
    path("addfutureexp", views.addexpense),
    path("paid/<id>", views.paid),
    path("delete/<id>", views.delete),
    path("update/<id>", views.updates),
    path("signup", views.handelsignup),
    path("login", views.handellogin),
    path("logout/", views.handellogout)


]
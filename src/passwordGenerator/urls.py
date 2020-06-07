from django.contrib import admin
from django.urls import path

from generator import views

urlpatterns = [
    path("", views.home, name="home"),
    path("password/", views.password, name="password"),
    path("admin/", admin.site.urls),
]

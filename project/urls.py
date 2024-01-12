from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls), # /admin/
    path('', include('recipes.urls')) # /.../
]

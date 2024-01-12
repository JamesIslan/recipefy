from django.urls import path

from recipes import views

urlpatterns = [
    path('', views.home),
    path('recipes/', views.recipe),
    path('recipes/<int:id>/', views.recipe),
]

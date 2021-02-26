from django.urls import path

from ex02 import views

urlpatterns = [
    path('init', views.index, name='index'),
    path('populate', views.populate, name='populate'),
    path('display', views.display, name="display"),
]
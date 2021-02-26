from django.urls import path

from ex import views

urlpatterns = [
    path('', views.home, name=''),
    path('inscription', views.inscription, name='login'),
    path('connexion', views.connexion, name='connexion'),
    path('deconnexion', views.deconnexion, name='deconnexion')
]

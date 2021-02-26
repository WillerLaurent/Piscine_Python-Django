"""D07 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ex.views import ArticleList, PublicationView, DetailsViews, FavouritesViews, UserCreate, PublishView
from django.views.generic import RedirectView
from django.contrib.auth import views


urlpatterns = [
    path('articles', ArticleList.as_view(template_name='articles.html'), name='articles'),
    path('', RedirectView.as_view(pattern_name='articles')),
    path('account/login', views.LoginView.as_view(), name='login'),
    path('account/logout', views.LogoutView.as_view(), name='logout'),
    path('publications', PublicationView.as_view(template_name='publications.html'), name='publications'),
    path('details/<int:pk>', DetailsViews.as_view(template_name='detail.html'), name='details'),
    path('favourites', FavouritesViews.as_view(template_name='favourites.html'), name='favourites'),
    path('register', UserCreate.as_view(template_name='register.html'), name='register'),
    path('new_publish', PublishView.as_view(template_name='new_publish.html'), name='new_publish'),
    path('admin/', admin.site.urls),
]

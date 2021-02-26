from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Article, UserFavouriteArticle
from django.views.generic.edit import FormView, CreateView
# from ex.forms import NewPublishForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy


class ArticleList(ListView):
    model = Article


class PublicationView(ListView):
    model = Article


class DetailsViews(DetailView):
    model = Article


class FavouritesViews(ListView):
    model = UserFavouriteArticle


class UserCreate(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('articles')


class PublishView(CreateView):
    model = Article
    fields = ['content', 'synopsis', 'title']
    success_url = reverse_lazy('publications')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PublishView, self).form_valid(form)


# class LoginView(FormView):
#     template_name = 'registration/login.html'
#     form_class = AuthenticationForm
#     success_url = 'articles'
#     user = User.username


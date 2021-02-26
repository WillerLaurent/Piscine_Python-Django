from django.db import models


class Tip(models.Model):
    auteur = models.CharField(max_length=32)
    contenu = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)

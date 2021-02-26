from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from ex.models import Tip


class Login(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(required=True, widget=forms.PasswordInput)

    def clean_password2(self):
        form_data = super(Login, self).clean()  # appliquer la validation de laclasse mère
        u = User.objects.filter(username=form_data['username'])  # recherche d'unicité
        if len(u) > 0:
            self.errors['username'] = ['Ce nom existe déjà']
        if form_data['password'] != form_data['password2']:
            self.errors['password'] = ["Les 2 mots de passe doivent être identiques"]
        return form_data


class Connect(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)


class TipForm(forms.Form):
    contenu = forms.CharField(label='Texte', max_length=1000)

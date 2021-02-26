from django import forms
from django.contrib.auth.models import User


# class Login(forms.Form):
#     username = forms.CharField(required=True)
#     password = forms.CharField(required=True, widget=forms.PasswordInput)


# class InscriptionForm(forms.Form):
#     username = forms.CharField(required=True)
#     password = forms.CharField(required=True, widget=forms.PasswordInput)
#     password2 = forms.CharField(required=True, widget=forms.PasswordInput)
#
#     def clean(self):
#         form_data = super(InscriptionForm, self).clean()#appliquer validation de la classe mere
#         u = User.objects.filter(username = form_data['username']) #recherche d'unicité
#         if len(u) > 0:
#             self.errors['username'] = ['Cet identifiant est déjà pris']
#         if form_data['password'] != form_data['password2']:
#             self.errors['password'] = ['les 2 mots de passe doivent être identiques']
#         return form_data

# class NewPublishForm(forms.Form):
#     content = forms.CharField(label='texte', max_length=1000)
#     synopsis = forms.CharField(label='texte', max_length=100)


from django import forms


class Formulaire (forms.Form):

    titre = forms.CharField(label="Titre", max_length=100)
    categorie = forms.CharField(label="Catégorie", max_length=100)
    youtube= forms.URLField(label="Vidéo", max_length=100)
    canva= forms.URLField(label="Fiche Recette", max_length=100)
    photo= forms.URLField(label="Photo", max_length=100)





from django.db import models
from django.template.defaultfilters import slugify


class Recettes (models.Model):
    PATISSERIE = "PT"
    PLAT = "PL"
    BOISSON = "BS"
    ENTREE = "ET"
    SAUCE = "SC"


    GENRES = [
        (PATISSERIE, "Pâtisserie"),
        (PLAT, "Plat"),
        (BOISSON, "Boisson"),
        (ENTREE, "Entrée"),
        (SAUCE, "Sauce"),
    ]
    titre = models.CharField(max_length=100)
    categorie = models.CharField(max_length=25, blank=True, choices=GENRES)
    slug= models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titre)
            super().save(*args,**kwargs)




from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Recettes
from .models_forms import Formulaire


def liste_recettes(request):
    recettes = Recettes.objects.all().order_by('titre')
    return render(request, 'library/recettes.html', {'recettes':recettes})

def fiche_recette(request, recettes_id):
    print("hello" +request.method)

    if request.method == "POST":
        ficherecette = Recettes.objects.get (pk=recettes_id)

        ficherecette.delete()

        return HttpResponseRedirect('/recettes')

    else:
        ficherecette = Recettes.objects.get(pk=recettes_id)
        return render(request, 'library/fiche_recette.html', {'recette':ficherecette})

def formulaire_saisie (request):

    if request.method == 'POST':

        formulaire= Formulaire(request.POST)

        if formulaire.is_valid():
            titre= formulaire.cleaned_data['titre']
            categorie= formulaire.cleaned_data['categorie']
            youtube= formulaire.cleaned_data['youtube']
            canva= formulaire.cleaned_data['canva']
            photo= formulaire.cleaned_data['photo']


            f= Recettes(titre=titre, categorie=categorie, youtube=youtube, canva=canva, photo=photo)
            f.save()
            return HttpResponseRedirect ('/recettes')

    else:
        formulaire= Formulaire()
        return render(request, 'library/formulaire.html', {'formulaire':formulaire})
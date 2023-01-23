from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Recettes


def liste_recettes(request):
    recettes = Recettes.objects.all().order_by('titre')
    return render(request, 'library/recettes.html', {'recettes':recettes})

def fiche_recette(request, recettes_id):
    ficherecette = get_object_or_404 (Recettes, pk=recettes_id)
    print(ficherecette)
    return render(request, 'library/fiche_recette.html', {'recette':ficherecette})

    video = (Recettes, Recettes.youtube)
    return render(request, {lien_video:video})
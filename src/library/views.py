from django.http import HttpResponse
from django.shortcuts import render
from .models import Recettes


def liste_recettes(request):
    recettes = Recettes.objects.all().order_by('titre')
    return render(request, 'library/recettes.html', {'recettes':recettes})

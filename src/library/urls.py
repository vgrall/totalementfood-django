
from django.urls import path
from . import views


app_name = 'liste_recettes'

urlpatterns = [

    path('', views.liste_recettes),
    path('<int:recettes_id>/', views.fiche_recette, name='fiche_recette')
]

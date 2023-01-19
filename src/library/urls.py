
from django.urls import path
from . import views


app_name = 'liste_recettes'

urlpatterns = [

    path('', views.liste_recettes),
]

from django.urls import path, include
from rest_framework import routers
from .views import (UserPokeViewSet,  
                    ListPokemonView, RetrievePokemonView,
                    ListItemView, ListBallView, 
                    ListPersonalityView, ListWazaView)

router = routers.DefaultRouter()

router.register("userpoke", UserPokeViewSet)

urlpatterns = [
    path('pokemons/', ListPokemonView.as_view(), name='pokemons'),
    path('pokemon/<int:pk>/', RetrievePokemonView.as_view(), name='pokemon'),
    path('items/', ListItemView.as_view(), name='items'),
    path('balls/', ListBallView.as_view(), name='balls'),
    path('personalities/', ListPersonalityView.as_view(), name='personalities'),
    path('wazas/', ListWazaView.as_view(), name='wazas'),
    path('', include(router.urls)),
]

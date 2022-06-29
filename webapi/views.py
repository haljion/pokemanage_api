from rest_framework import status, permissions, generics, viewsets, filters
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Pokemon, Item, Ball, Personality, Waza, UserPoke
from .serializers import (PokemonSerializer, ItemSerializer,
                                BallSerializer, PersonalitySerializer, 
                                WazaSerializer, UserPokeSerializer)


class UserPokeViewSet(viewsets.ModelViewSet):
    queryset = UserPoke.objects.all()
    serializer_class = UserPokeSerializer
    filter_fields = ('user_id', )


class ListPokemonView(generics.ListAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer


class RetrievePokemonView(generics.RetrieveAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer


class ListItemView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ListBallView(generics.ListAPIView):
    queryset = Ball.objects.all()
    serializer_class = BallSerializer


class ListPersonalityView(generics.ListAPIView):
    queryset = Personality.objects.all()
    serializer_class = PersonalitySerializer


class ListWazaView(generics.ListAPIView):
    queryset = Waza.objects.all()
    serializer_class = WazaSerializer

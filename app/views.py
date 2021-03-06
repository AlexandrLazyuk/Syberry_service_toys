from rest_framework import viewsets
from .models import Toy, Game
from .serializers import GameSerializer, ToySerializer


class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows games to be viewed or edited.
    """
    queryset = Game.objects.all().order_by('-id')
    serializer_class = GameSerializer


class ToyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows toys to be viewed or edited.
    """

    queryset = Toy.objects.all().order_by('-id')
    serializer_class = ToySerializer


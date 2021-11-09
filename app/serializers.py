from rest_framework import serializers
from .models import Game, Toy


class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'note']


class ToySerializer(serializers.HyperlinkedModelSerializer):
    games = GameSerializer(many=True)

    class Meta:
        model = Toy
        fields = ['id', 'name', 'games']
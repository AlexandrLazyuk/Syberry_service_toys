from rest_framework import serializers
from .models import Game, Toy


class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'name']


class ToySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Toy
        fields = ['id', 'name']
from django.contrib import admin
from .models import Toy, Game


@admin.register(Toy)
class ToyAdmin(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id',)
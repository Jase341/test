from django.contrib import admin
from .models import Games, NextGame,LastWeekGame, Message, ImageProofs

# Register your models here.
admin.site.register(Games)
admin.site.register(NextGame)
admin.site.register(LastWeekGame)
admin.site.register(Message)
admin.site.register(ImageProofs)

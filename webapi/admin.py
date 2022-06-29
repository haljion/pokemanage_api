from django.contrib import admin
from .models import Pokemon, Item, Ball, Personality, Waza, UserPoke


admin.site.register(Pokemon)
admin.site.register(Item)
admin.site.register(Ball)
admin.site.register(Personality)
admin.site.register(Waza)
admin.site.register(UserPoke)

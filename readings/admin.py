from django.contrib import admin
from .models import Reading, Card, Profile, CardInstance


class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'arcana', 'suit', 'meaning', 'r_meaning', 'description', 'image')
    list_filter = ('arcana', 'suit')
    search_fields = ('id', 'name')

    fieldsets = (
        ('Bendra informacija apie kortą', {
        'fields': ('id', 'name', 'arcana', 'suit', 'image')
        }),
        ('Kortos aprašymas ir reikšmės', {
        'fields': ('description', 'meaning', 'r_meaning')
        })
    )


class ReadingAdmin(admin.ModelAdmin):
    list_display = ('date', 'cards', 'id', 'user')
    list_editable = ('cards',)
    list_filter = ('date', 'user')
    search_fields = ('cards', 'id', 'user')


admin.site.register(Reading, ReadingAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(CardInstance)
admin.site.register(Profile)
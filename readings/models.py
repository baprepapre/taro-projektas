from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

import uuid

class Card(models.Model):
    ARCANA_CHOICES = (
    ('minor', 'Mažieji arkanai'),
    ('major', 'Didieji arkanai')
    )

    SUITS_CHOICES = (
    ('none', ''),
    ('wands', 'Lazdos'),
    ('cups', 'Taurės'),
    ('swords', 'Kardai'),
    ('pentacles', 'Monetos')
    )

    id = models.IntegerField(primary_key=True, help_text='Kortos seka kaladėje')
    image = models.ImageField('Nuotrauka', null=True)
    name = models.CharField('Pavadinimas', max_length=100, help_text='Kortos pavadinimas')
    description = models.TextField('Aprašymas', max_length=5000, help_text='Išsamus simbolizmo ir reikšmės aprašymas')
    meaning = models.TextField('Reikšmė', max_length=1000, help_text='Trumpas pagrindinių kortos reikšmių apibūdinimas')
    r_meaning = models.TextField('Reikšmė - apversta', max_length=1000, help_text='Trumpas pagrindinių apverstos kortos reikšmių apibūdinimas')
    arcana = models.CharField(
        'Arkanai',
        max_length=5, 
        choices=ARCANA_CHOICES,
        help_text='Pasirinkite arkanus',
        null=True
    )
    suit = models.CharField(
        'Rūšis',
        max_length=9, 
        choices=SUITS_CHOICES,
        null=True,
        help_text="Pasirinkite rūšį",
    )

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('card-detail', args=[str(self.id)])

    class Meta:
        ordering = ['id']
    

class CardInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    card = models.CharField('Korta', max_length=200, help_text='Specifinis kortos egzempliorius, gautas būrimo metu')
    position = models.CharField('Kortos pozicija', max_length=10, help_text='Pozicija, kuria korta iškrito būrimo metu')

    def __str__(self):
        return f'{self.card}{self.position}'
    
    def display_info(self):
        return f'{self.card.arcana} {self.card.suit}'
    

class Reading(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    type = models.CharField('Tipas', max_length=50, help_text='Informacija apie būrimą', null=True)
    cards = models.CharField('Kortos', max_length=500, help_text='Trumpa informacija apie kortas, ištrauktas būrimo metu')
    date = models.DateTimeField('Sukurta', auto_now=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.cards


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return f'{self.user.username} profile'

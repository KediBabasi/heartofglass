from django.db import models

# Create your models here.

UCRETLENDIRME = [
    ('faturali', 'Faturalı'),
    ('faturasiz', 'Faturasız'),
]

class Card (models.Model):
    tarife_adi = models.CharField(max_length=50)
    tarife_slug = models.CharField(max_length=20)
    ucretlendirme = models.CharField(choices=UCRETLENDIRME, max_length=9)
    ana_tarife = models.CharField(max_length=40)
    fiyat = models.FloatField(null=True, blank=True)
    taahhutsuz_fiyat = models.FloatField(null=True, blank=True)
    sms = models.PositiveIntegerField(null=True, blank=True)
    dakika = models.PositiveIntegerField(null=True, blank=True)
    internet = models.FloatField(null=True, blank=True)


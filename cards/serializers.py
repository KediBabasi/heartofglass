from django.contrib.auth.models import User
from rest_framework import serializers
from cards.models import Card


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Card
        fields = ('tarife_adi', 'tarife_slug', 'ucretlendirme', 'ana_tarife', 'fiyat', 'taahhutsuz_fiyat', 'sms', 'dakika', 'internet')

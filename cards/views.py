from django.contrib.auth.models import User
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from cards.models import Card
from cards.serializers import UserSerializer, CardSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class CardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Card.objects.all()
    serializer_class = CardSerializer


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def cardqueryslug(request, slug):
    card = Card.objects.get(tarife_slug=slug)
    serializer = CardSerializer(card, many=False)
    return Response(serializer.data)

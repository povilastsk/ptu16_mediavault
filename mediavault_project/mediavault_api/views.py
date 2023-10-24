from rest_framework import generics
from . import models, serializers


class BandList(generics.ListCreateAPIView):
    queryset = models.Band.objects.all()
    serializer_class = serializers.BandSerializer

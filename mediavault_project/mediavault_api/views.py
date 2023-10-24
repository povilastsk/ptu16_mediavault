from rest_framework import generics
from . import models, serializers


class BandList(generics.ListAPIView):
    queryset = models.Band.objects.all()
    serializer_class = serializers.BandSerializer

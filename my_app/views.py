from rest_framework import generics
from rest_framework.response import Response

from . import models, serializers, tasks


class DataAPIView(generics.ListCreateAPIView):
    queryset = models.Data.objects.all()
    serializer_class = serializers.DataSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("OK!")


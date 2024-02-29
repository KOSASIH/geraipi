from rest_framework import viewsets

from frontend.serializers import VillageSerializer
from master.models import Village


class VillagerViewset(viewsets.ModelViewSet):
    queryset = Village.objects.all()
    serializer_class = VillageSerializer

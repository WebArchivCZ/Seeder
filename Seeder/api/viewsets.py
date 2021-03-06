import source
import blacklists

from rest_framework import viewsets
from rest_framework import mixins as rf_mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from . import serializers


class CategoryViewSet(rf_mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = serializers.CategorySerializer
    queryset = source.models.Category.objects.all()


class SourceViewSet(rf_mixins.RetrieveModelMixin, rf_mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    """
    Viewset that does not implement listing, deleting and creating of sources.
    """
    serializer_class = serializers.SourceSerializer
    queryset = source.models.Source.objects.all()
    http_method_names = ['head', 'get', 'patch']


class SeedViewSet(viewsets.GenericViewSet, rf_mixins.RetrieveModelMixin,
                  rf_mixins.UpdateModelMixin):
    """
    Viewset for updating seeds
    """
    serializer_class = serializers.SeedSerializer
    queryset = source.models.Seed.objects.all()


class BlacklistViewSet(viewsets.GenericViewSet, rf_mixins.RetrieveModelMixin,
                       rf_mixins.ListModelMixin):
    serializer_class = serializers.BlacklistSerializer
    queryset = blacklists.models.Blacklist.objects.all()

    @action(methods=['get'], detail=False)
    def lastchanged(self, request):
        return Response({
            'lastChanged': blacklists.models.Blacklist.last_change(),
        })

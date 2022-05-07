from rest_framework import mixins, viewsets


class ListRetrieveGeneric(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    pass

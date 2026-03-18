from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from ..filters import PrepaymentMethodFilter
from ..models import PrepaymentMethod
from ..serializers.prepayment_method import PrepaymentMethodSerializer


@extend_schema(tags=["Tax Compliance: Prepayment Method"])
class PrepaymentMethodViewSet(viewsets.ModelViewSet):
    queryset = PrepaymentMethod.objects.all()
    serializer_class = PrepaymentMethodSerializer

    @property
    def filterset_class(self):
        return PrepaymentMethodFilter

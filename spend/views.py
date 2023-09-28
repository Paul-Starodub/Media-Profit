from typing import Optional

from django.db.models import Sum, Subquery, OuterRef
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from revenue.models import RevenueStatistic
from spend.models import SpendStatistic
from spend.serializers import SpendStatisticSerializer


class SpendStatisticsView(APIView):
    def get(self, request: Request, format: Optional[str] = None) -> Response:
        subquery = (
            RevenueStatistic.objects.filter(spend=OuterRef("pk"))
            .values("spend")
            .annotate(total_revenue=Sum("revenue"))
            .values("total_revenue")[:1]
        )

        queryset = SpendStatistic.objects.values("date", "name").annotate(
            total_spend=Sum("spend"),
            total_impressions=Sum("impressions"),
            total_clicks=Sum("clicks"),
            total_conversion=Sum("conversion"),
            total_revenue=Subquery(subquery),
        )

        serializer = SpendStatisticSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

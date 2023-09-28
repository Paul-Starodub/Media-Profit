from rest_framework import serializers

from spend.models import SpendStatistic


class SpendStatisticSerializer(serializers.ModelSerializer):
    total_spend = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True
    )
    total_revenue = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True
    )
    total_impressions = serializers.IntegerField(read_only=True)
    total_clicks = serializers.IntegerField(read_only=True)
    total_conversion = serializers.IntegerField(read_only=True)

    class Meta:
        model = SpendStatistic
        fields = (
            "name",
            "date",
            "total_spend",
            "total_revenue",
            "total_impressions",
            "total_clicks",
            "total_conversion",
        )

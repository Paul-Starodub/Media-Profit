from django.urls import path

from spend.views import SpendStatisticsView

urlpatterns = [
    path(
        "",
        SpendStatisticsView.as_view(),
        name="spend-statistics",
    ),
]

app_name = "spends"

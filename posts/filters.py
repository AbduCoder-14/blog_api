from django_filters import rest_framework as filters
from .models import Vote


class VoteAnalyticsFilter(filters.FilterSet):
    class Meta:
        model = Vote
        fields = {"created_at": ["gte", "lte"]}

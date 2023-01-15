from django_filters import FilterSet, CharFilter

from goal.models import Goal


class PostFilter(FilterSet):
    goal = CharFilter(lookup_expr="icontains")
    user = CharFilter(field_name="user__email", lookup_expr="icontains")

    class Meta:
        model = Goal
        fields = ["goal", "user__email"]

    def __init__(self, *args, **kwargs):
        super(PostFilter, self).__init__(*args, **kwargs)
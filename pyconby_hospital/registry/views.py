from typing import Optional, List, Tuple

from django.db.models import QuerySet
from django.views.generic.list import ListView

from . import models


class VisitListView(ListView):
    model = models.Visit

    def get_queryset(self):
        qs = super().get_queryset()
        return self._optimize_query(qs)

    def _optimize_query(self, qs: QuerySet, blocked_user: Optional[List[Tuple[int, Optional[int]]]] = None):
        return qs.select_related()

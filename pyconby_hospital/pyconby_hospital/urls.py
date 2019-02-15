from django.contrib import admin
from django.urls import include, path
from django.conf import settings
import debug_toolbar


from registry.views import VisitListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),

    path('visits/', VisitListView.as_view(), name='visits-list'),
]

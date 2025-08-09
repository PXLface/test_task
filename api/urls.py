from django.urls import path
from .views import DDSListView

urlpatterns = [
    path('dds/', DDSListView.as_view(), name='dds-list'),
]
from django.urls import path
from .views import DDSCreateView, DDSListView

urlpatterns = [
    path('dds', DDSListView.as_view(), name='dds-list'),
    path('dds/post/', DDSCreateView.as_view(), name='dds_create'),
]
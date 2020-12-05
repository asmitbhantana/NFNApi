from django.urls import path

from Faq.views import FaqViewSet

app_name = "faq"

urlpatterns = [
    path('list/', FaqViewSet.as_view({'get': 'list', 'post': 'create'}), name="all"),
    path('update/<int:pk>/', FaqViewSet.as_view({'put': 'update'}), name="update"),
    path('partial-update/<int:pk>/', FaqViewSet.as_view({'patch': 'partial_update'}), name="patch"),
    path('delete/<int:pk>/', FaqViewSet.as_view({'delete': 'destroy'}), name="delete"),
]

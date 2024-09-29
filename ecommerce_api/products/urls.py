from django.urls import path
from .views import (
    ProductListCreateView,
    ProductDetailView,
    ProductSearchView,
)

urlpatterns = [
    path('products/search/', ProductSearchView.as_view(), name='product-search'),
    path('products/', ProductListCreateView.as_view(), name='product-list'),  # Listing and creating
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),  # Detail view
]

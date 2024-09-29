from django.shortcuts import render
from django.db.models import Q
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .serializers import ProductSerializer, OrderSerializer, CategorySerializer
from .models import Product, Order, Category
from users.permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

# Custom Pagination Class
class ProductSearchPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

# Product List and Create View
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    pagination_class = ProductSearchPagination

# Product Detail View
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]

# Product Search View with Filtering
class ProductSearchView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['category', 'price', 'stock_quantity']  # Additional fields can be added
    search_fields = ['name', 'category__name']  # Ensure 'category__name' is correct if using ForeignKey
    pagination_class = ProductSearchPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        q = self.request.query_params.get('q', None)

        # Filter by price range if provided
        if min_price and max_price:
            queryset = queryset.filter(price__range=(min_price, max_price))

        # If 'q' is provided, filter by name and category
        if q:
            queryset = queryset.filter(
                Q(name__icontains=q) | 
                Q(category__name__icontains=q)
            )

        return queryset

# Order Create View
class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

# Product Create, Update, Delete View
class ProductCreateUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

# Category List and Create View
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
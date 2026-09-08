from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .pagination import ProductPagination
from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView
from .permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet
class ProductListView(ListAPIView):

    queryset= Product.objects.all()
    serializer_class = ProductSerializer
    def get_permissions(self):
        if self.request.method=='GET':
            return []
        return [IsAuthenticated()]
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(RetrieveUpdateDestroyAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def get_permissions(self):
        if self.request.method=='GET':
            return []
        if self.request.method=='DELETE':
            return [IsAdminUser()]
        return [IsAuthenticated()]


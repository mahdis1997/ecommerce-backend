from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Cart
from .serializers import CartSerializer
from rest_framework.response import Response


class CartViewSet(ModelViewSet):
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
    serializer_class = CartSerializer
    def create(self, request, *args, **kwargs):
        cart = Cart.objects.filter(user=request.user).first()
        if not cart:
            cart=Cart.objects.create(user=request.user)
            serializer=CartSerializer(cart)
        return Response(serializer.data)


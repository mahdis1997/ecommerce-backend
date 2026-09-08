from rest_framework import serializers
from .models import CartItem,Cart


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=CartItem
        fields=["id","product","quantity"]

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model:Cart
        fields=["id","user","create_at"]

from rest_framework import serializers
from .models import CartItem,Cart,OrderItem,Order,Payment


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=CartItem
        fields=["id","product","quantity"]

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields=["id","user","created_at"]
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderItem
        fields=["id","product","quantity","price"]

class OrderSerializer(serializers.ModelSerializer):
    items=OrderItemSerializer(many=True,read_only=True)
    class Meta:
        model=Order
        fields = ["id", "status","total_price","created_at", "items"]

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        moder=Payment
        fields =["id","order","amount","status","authority","ref_id","created_at"]
        read_only_fields=["amount","status","authority","ref_id","created_at"]
from rest_framework import serializers
from .models import Product
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=["id","name","price","stock"]
    def validate_price(self,value):
        if value<=0:
            raise serializers.ValidationError(
                "price must be grate than zero"
            )
        return value

    def validate_stock(self,value):
        if value<0:
            raise serializers.ValidationError(
                "stock not be smaller than zero"
            )
        return value

    def validate_name(self, value):

        if not value.strip():
            raise serializers.ValidationError(
                "Name cannot be empty."
            )

        return value


from rest_framework import serializers

from Shopping_Cart.models import Product


class ListSerializer(serializers.Serializer):
     name = serializers.CharField(max_length=100, required=False)


     def validate(self, attrs):
        name = attrs.get("name")
        return attrs


class ProductSerializer(serializers.ModelSerializer):
   customer_name = serializers.CharField(source="customer.name")

   class Meta:
        model = Product
        fields = [
                    "name",
                    "customer_name",
                    "availability"
                 ]


class ListProductSerializer(serializers.ModelSerializer):
   customer_name = serializers.CharField(source="customer.name")

   class Meta:
        model = Product
        fields = [
                    "name",
                    "customer_name"
                 ]


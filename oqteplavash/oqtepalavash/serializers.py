from rest_framework import serializers
from .models import Category,Product,Branche


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id','name','image','price',]

class CategorySerializer(serializers.ModelSerializer):
    products=ProductSerializer(many=True,read_only=True)

    class Meta:
        model=Category
        fields=['id','name','image','products']


class BrancheSerializer(serializers.ModelSerializer):
    class Meta:
        model=Branche
        fields=['id','name','image','address']

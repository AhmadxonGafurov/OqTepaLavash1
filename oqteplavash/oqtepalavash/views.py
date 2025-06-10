from django.shortcuts import render
from rest_framework import viewsets
from .models import Category,Product,Branche
from .serializers import CategorySerializer,ProductSerializer,BrancheSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.filter(status=True)
    serializer_class=CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.filter(status=True)
    serializer_class=ProductSerializer

class BrancheViewSet(viewsets.ModelViewSet):
    queryset=Branche.objects.filter(status=True)
    serializer_class=BrancheSerializer
from django.shortcuts import render

def frontend_view(request):
    return render(request, 'index.html')

from rest_framework import routers
from .views import CategoryViewSet,ProductViewSet,BrancheViewSet
from django.urls import path,include

router=routers.DefaultRouter()
router.register(r'category',CategoryViewSet,basename='category')
router.register(r'product',ProductViewSet,basename='product')
router.register(r'branche',BrancheViewSet,basename='branche')

urlpatterns=[
    path('',include(router.urls)),
]




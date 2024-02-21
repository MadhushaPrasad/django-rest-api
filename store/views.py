from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer


@api_view(['GET'])
def get_all_projects(request):
    querySet = Product.objects.all()
    serializer = ProductSerializer(querySet, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_product_detail(request,id):
    product = get_object_or_404(Product,pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)
        
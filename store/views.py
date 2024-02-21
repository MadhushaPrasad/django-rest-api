from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer


@api_view(['GET'])
def get_all_projects(request):
    return Response("All projects")


@api_view(['GET'])
def get_product_detail(request,id):
    product =  Product.objects.get(pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)
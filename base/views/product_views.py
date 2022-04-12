from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Product
from base.serializers import ProductSerializer


@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def get_product(request, pk):
    product = None
    try:
        product = Product.objects.get(pk=pk)
    except Exception:
        return Response({'error': True, 'message': 'Product not found'}, status=status.HTTP_400_BAD_REQUEST)
    if product != None:
        serializer = ProductSerializer(product, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({'error': True}, status=status.HTTP_400_BAD_REQUEST)
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from products.models import Product, Cart, FavoriteProduct, ProductTag, Review


from products.models import Product, Review

from products.serializers import ProductSerializer, ReviewSerializer



@api_view(['GET', 'POST'])
def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = serializer.save()
            return Response({"id": product.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(["GET"])
def product_view(request, pk):
    obj = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(obj)
    return Response(serializer.data)

@api_view(["GET", "POST"])
def reviews_view(request):
    if request.method == "GET":
        serializer = ReviewSerializer(Review.objects.all(), many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ReviewSerializer(data=request.data, context={'request': request})
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
@api_view(['GET', 'POST'])
def cart_view(request):
    user_cart, _ = Cart.objects.get_or_create(user=request.user)

    if request.method == 'GET':
        products = user_cart.products.all()
        return Response({'cart_items': [product.id for product in products]})

    elif request.method == 'POST':
        product_id = request.data.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        user_cart.products.add(product)
        return Response({'message': 'Product added to cart'}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def product_tag_view(request):
    if request.method == 'GET':
        product_id = request.query_params.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        tags = product.tags.all()
        return Response({'tags': [tag.name for tag in tags]})

    elif request.method == 'POST':
        product_id = request.data.get('product_id')
        tag_name = request.data.get('tag_name')

        product = get_object_or_404(Product, id=product_id)
        tag, created = ProductTag.objects.get_or_create(name=tag_name)
        product.tags.add(tag)

        return Response({'message': 'Tag added to product'}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def favorite_product_view(request):
    if request.method == 'GET':
        favorites = FavoriteProduct.objects.filter(user=request.user)
        return Response({'favorites': [fav.product.id for fav in favorites]})

    elif request.method == 'POST':
        product_id = request.data.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        FavoriteProduct.objects.get_or_create(user=request.user, product=product)
        return Response({'message': 'Product added to favorites'}, status=status.HTTP_201_CREATED)



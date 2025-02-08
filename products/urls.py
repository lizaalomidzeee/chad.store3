from django.urls import path
from products.views import products_view, reviews_view, product_view, cart_view, product_tag_view, favorite_product_view

urlpatterns = [
    path('products/', products_view, name="products"),
    path('products/<int:pk>', product_view, name='product'),
    path('reviews/', reviews_view, name="reviews"),
    path('cart/', cart_view, name='cart_view'),
    path('product-tags/', product_tag_view, name='product_tag_view'),
    path('favorites/', favorite_product_view, name='favorite_product_view'),
]
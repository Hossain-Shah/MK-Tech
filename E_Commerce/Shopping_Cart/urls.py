from django.urls import path
 
from Shopping_Cart.views import ProductDetail
from Shopping_Cart.views import ProductView
from Shopping_Cart.views import ProductList


urlpatterns = [
    path('product', ProductList.as_view()),
    path('api/product', ProductView.as_view()),
    path('product/<int:pk>', ProductDetail.as_view())
]
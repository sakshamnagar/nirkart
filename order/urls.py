from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    
    path('cart/add/<slug:slug>/', views.cart_add, name='cart_add'),
    path('cart/buy-now/<slug:slug>/', views.buy_now, name='buy_now'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/',views.cart_detail, name='cart'),
    path('checkout/',views.checkout, name='checkout'),
    path('review/<str:name>', views.review, name='review'),
    path('test/', views.test, name='test'),

]
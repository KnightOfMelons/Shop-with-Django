from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from main import views
from shop.views import ProductsListView, ProductsDetailView, add_item_to_cart, \
    cart_view, CartDeleteItem, make_order, history_page

urlpatterns = [
    path('', ProductsListView.as_view(), name='shop'),
    path('cart_view/', cart_view, name='cart_view'),
    path('detail/<int:pk>/', ProductsDetailView.as_view(),
         name='shop_detail'),
    path('add-item-to-cart/<int:pk>', add_item_to_cart, name='add_item_to_cart'),
    path('delete_item/<int:pk>', CartDeleteItem.as_view(), name='cart_delete_item'),
    path('make-order/', make_order, name='make_order'),
    path('history/', history_page, name='history_orders')
    # path('history/', HistoryOfOrders.as_view() ,name='history_orders'),
]

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from main import views
from shop.views import ProductsListView, ProductsDetailView, add_item_to_cart, \
    cart_view, CartDeleteItem, make_order, history_page, male_category_page, female_category_page,\
    top_category_page, bottom_category_page, accessories_category_page

urlpatterns = [
    path('', ProductsListView.as_view(), name='shop'),
    path('cart_view/', cart_view, name='cart_view'),
    path('detail/<int:pk>/', ProductsDetailView.as_view(),
         name='shop_detail'),
    path('add-item-to-cart/<int:pk>', add_item_to_cart, name='add_item_to_cart'),
    path('delete_item/<int:pk>', CartDeleteItem.as_view(), name='cart_delete_item'),
    path('make-order/', make_order, name='make_order'),
    path('history/', history_page, name='history_orders'),
    path('male_category/', male_category_page, name='male_category'),
    path('female_category/', female_category_page, name='female_category'),
    path('top_category/', top_category_page, name='top_category'),
    path('bottom_category/', bottom_category_page, name='bottom_category'),
    path('accessories_category', accessories_category_page, name='accessories_category')
]

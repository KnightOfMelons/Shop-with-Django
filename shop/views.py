from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from django.views.generic import ListView, DetailView, DeleteView

from shop.forms import AddQuantityForm
from shop.models import Product, Order, OrderItem


class ProductsListView(ListView):
    model = Product
    template_name = 'shop/shop.html'


class ProductsDetailView(DetailView):
    model = Product
    template_name = 'shop/shop-single.html'


@login_required(login_url=reverse_lazy('login'))
def add_item_to_cart(request, pk):
    if request.method == 'POST':
        quantity_form = AddQuantityForm(request.POST)
        if quantity_form.is_valid():
            quantity = quantity_form.cleaned_data['quantity']
            if quantity:
                cart = Order.get_cart(request.user)
                product = get_object_or_404(Product, pk=pk)
                cart.orderitem_set.create(product=product,
                                          quantity=quantity,
                                          price=product.price)
                cart.save()
                return redirect('cart_view')
        else:
            pass
    return redirect('shop')


@login_required(login_url=reverse_lazy('login'))
def cart_view(request):
    cart = Order.get_cart(request.user)
    items = cart.orderitem_set.all()
    context = {
        'cart': cart,
        'items': items,
    }
    return render(request, 'shop/cart.html', context)

@method_decorator(login_required, name='dispatch')
class CartDeleteItem(DeleteView):
    model = OrderItem
    template_name = 'shop/cart.html'
    success_url = reverse_lazy('cart_view')

    # Проверка доступа
    def get_queryset(self):
        qs = super().get_queryset()
        qs.filter(order__user=self.request.user)
        return qs


@login_required(login_url=reverse_lazy('login'))
def make_order(request):
    cart = Order.get_cart(request.user)
    cart.make_order()
    return redirect('shop')

@login_required(login_url=reverse_lazy('login'))
def history_page(request):
    history = Order.get_history(request.user)
    context = {
        'history': history,
    }
    return render(request, 'shop/history.html', context)


def male_category_page(request):
    category = Product.get_all_by_male_cat(request.user)
    context = {
        'category': category,
    }
    return render(request, 'shop/male_cat.html', context)

def female_category_page(request):
    category = Product.get_all_by_female_cat(request.user)
    context = {
        'category': category,
    }
    return render(request, 'shop/female_cat.html', context)

def top_category_page(request):
    category = Product.get_all_by_TOP(request.user)
    context = {
        'category': category,
    }
    return render(request, 'shop/top_cat.html', context)

def bottom_category_page(request):
    category = Product.get_all_by_BOTTOM(request.user)
    context = {
        'category': category,
    }
    return render(request, 'shop/bottom_cat.html', context)

def accessories_category_page(request):
    category = Product.get_all_by_ACCESSORIES(request.user)
    context = {
        'category': category,
    }
    return render(request, 'shop/accessories_cat.html', context)

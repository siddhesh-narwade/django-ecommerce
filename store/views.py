from django.shortcuts import render
from django.http import JsonResponse
from .models import Product, Order, OrderItem
import json

def store(request):
    products = Product.objects.all()
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(customer=request.user, complete=False)
        cartItems = order.get_cart_items
    else:
        cartItems = 0
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/store.html', context)

def cart(request):
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(customer=request.user, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(customer=request.user, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/checkout.html', context)

def update_item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = request.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

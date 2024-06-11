from django.shortcuts import render, redirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from .models import Order
from .models import OrderItem
from .forms import OrderCreateForm
from cart.models import Cart

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if request.user.is_authenticated:
                order.user = request.user
            order.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
            return redirect('order:order_created', order_id=order.id)
    else:
        if request.user.is_authenticated:
            initial_data = {
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'phone': request.user.phone,  # Assuming phone is in user's profile
                'address': request.user.address,  # Assuming address is in user's profile
                'postal_code': request.user.postal_code,  # Assuming postal_code is in user's profile
                'city': request.user.city,  # Assuming city is in user's profile
            }
            form = OrderCreateForm(initial=initial_data)
        else:
            form = OrderCreateForm()
    return render(request, 'order/create.html', {'cart': cart, 'form': form})


def order_created(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order/created.html', {'order': order})

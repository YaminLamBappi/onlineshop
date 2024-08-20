from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order
from .models import OrderItem
from .forms import OrderCreateForm
from cart.models import Cart


@login_required
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST, user=request.user)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()  # Clear the cart after saving the order
            return redirect('order:order_history')  # Redirect to order history
    else:
        form = OrderCreateForm(user=request.user)

    return render(request, 'order/create.html', {'cart': cart, 'form': form})


def order_created(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order/created.html', {'order': order})


@login_required
def order_history(request):
    orders = request.user.orders.all()
    return render(request, 'order/order_history.html', {'orders': orders})

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'order/order_detail.html', {'order': order})
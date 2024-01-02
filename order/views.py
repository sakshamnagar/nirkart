from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from myapp.models import Item
from account.models import Address
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.contrib import messages
from .models import DeliveryCharges, Order, Reviews
from .forms import ReviewForm
from django.contrib.auth.models import User


def cart_add(request, slug):
    cart = Cart(request)
    product = Item.objects.get(slug=slug)
    if product.quantity > 0:
        cart.add(product=product)
        messages.success(request, "item added to cart")
    else:
            messages.error(request,'Opps! It seems that there are no more items in stock.')
    return redirect('myapp:product_detail', slug = slug )


def buy_now(request,slug):
    cart = Cart(request)
    product = Item.objects.get(slug=slug)
    slug = product.slug
    if product.quantity > 0:
        cart.add(product=product)
        messages.success(request, "item added to cart")
    else:
            messages.error(request,'Opps! It seems that there are no more items in stock.')
    return redirect('order:cart')



def item_clear(request, id):
    cart = Cart(request)
    product = Item.objects.get(id=id)
    cart.remove(product)
    messages.error(request,'Item removed')
    return redirect("order:cart")



def item_increment(request, id):
    cart = Cart(request)
    product = Item.objects.get(id=id)
    for key,value in request.session['cart'].items():
        if value['quantity'] <= product.quantity:
            cart.add(product=product)
            messages.success(request,'Item added!')
        else:
            messages.error(request,'Opps! It seems that there are no more items in stock.')
    
    return redirect("order:cart")



def item_decrement(request, id):
    cart = Cart(request)
    product = Item.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("order:cart")



def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("order:cart")



def cart_detail(request):
    delivery = DeliveryCharges.objects.get(delivery=40)
    return render(request, 'order/cart.html')

@login_required
def checkout(request):
    cart = Cart(request)
    delivery = DeliveryCharges.objects.get(delivery=40)
    user_address = Address.objects.filter(user=request.user)
    add_id = request.GET.get('useraddress')
    print(add_id)
    if request.method == 'POST':
        address_id = request.POST.get('useraddress')
        address1 = request.POST.get('address')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        state = request.POST.get('state') 
        zip_code = request.POST.get('zip')

        if Address.objects.filter(id=address_id).exists():
            add = Address.objects.filter(id=address_id).first()
            address1 = add.address
            address2 = add.address2
            state = add.state
            city = add.city
            zip_code = add.zip_code

        if request.POST.get('save') == 'on':
            Address.objects.create(user=request.user,address=address1,address2=address2,state=state,city=city,zip_code=zip_code)


        for key,value in request.session['cart'].items():
            item_image = value['image']
            item_id = value['product_id']
            item_name = value['name']
            item_price = value['price']
            item_discounted_price = value['discounted_price']
            item_quantity = value['quantity']
            item_discount = value['discount']
            item_vendor = value['vendor']
            order = Order.objects.create(
                buyer = request.user,
                item_image = item_image,
                item_id = item_id,
                item_name = item_name,
                item_price = item_price,
                item_discounted_price = item_discounted_price,
                item_quantity = item_quantity,
                item_discount = item_discount,
                item_vendor = item_vendor,
                address1 = address1,
                address2 = address2,
                state = state,
                city = city,
                zip_code = zip_code)
        cart.clear()
        return render(request,'order/order_confirmation.html',{'order':order})

    return render(request,'order/checkout.html',{'cart':cart,'user_address':user_address})


@login_required
def test(request):
    address = Address.objects.filter(user=request.user)
    return render(request,'order/test.html', {'address':address})


@login_required
def review(request,name):
    form = ReviewForm()
    order = Order.objects.filter(item_name=name)
    items = Item.objects.get(name=name)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.item = items
            review.save()
            order = Order.objects.filter(item_name=name).update(review=True)
            messages.success(request,"Review Submitted!")
            return redirect("my-reviews")
        else:
            messages.error(request,'Please rate the item between 0 to 5.')
    else:
        form = ReviewForm()
    return render(request,'order/reviews.html', {"form":form, "items":items})
from cart.cart import Cart
from .models import DeliveryCharges

def cart_total_amount(request):
	cart = Cart(request)
	total_bill = 0.0
	bill_without_discount = 0.0

	for key,value in request.session['cart'].items():
		bill_without_discount = bill_without_discount + float(value['price']) * float(value['quantity'])
		

	for key,value in request.session['cart'].items():
		total_bill = total_bill + (float(value['discounted_price']) * value['quantity'])

	discount = bill_without_discount - total_bill

	if total_bill > 500:
		delivery_charges = DeliveryCharges.objects.get(delivery=0.0)
	else:
		delivery_charges = DeliveryCharges.objects.get(delivery=40.0)

	net = total_bill+delivery_charges.delivery
	
	return {'cart_total_amount' : total_bill, 'delivery':delivery_charges, 'bill_without_discount':bill_without_discount, 'discount': discount, 'net': net} 
	


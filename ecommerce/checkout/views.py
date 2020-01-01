from django.shortcuts import render,redirect
from cart.models import Order, Cart
from . models import BillingForm, BillingAddress
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
# Create your views here.

# /***************************************************************************************
# *    Title: <MANASCODE>
# *    Author: <Manas Paul>
# *    Date: <21 August 2019>
# *    Code version: <python>
# *    Availability: <https://manascode.com/django-ecommerce-website-tutorial-part-one/>
# *   Edited by: Ablehulu Debebe
# ***************************************************************************************/

@login_required
def checkout(request):
	# Checkout view
	form = BillingForm(request.POST or None)
	if request.method == 'POST':
		form.save(commit=False)
		form.instance.user = request.user
		form.save()
		return redirect('/')

	order_qs = Order.objects.filter(user= request.user, ordered=False)
	order_items = order_qs[0].orderitems.all()
	order_total = order_qs[0].get_totals()
	context = {"form": form, "order_items": order_items, "order_total": order_total}
	return render(request, 'checkout/index.html', context)

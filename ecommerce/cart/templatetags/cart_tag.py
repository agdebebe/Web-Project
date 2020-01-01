from django import template
from cart.models import Order

register = template.Library()

# /***************************************************************************************
# *    Title: <MANASCODE>
# *    Author: <Manas Paul>
# *    Date: <21 August 2019>
# *    Code version: <python>
# *    Availability: <https://manascode.com/django-ecommerce-website-tutorial-part-one/>
# *   Edited by: Ablehulu Debebe
# ***************************************************************************************/

@register.filter
def cart_total(user):
    order = Order.objects.filter(user=user, ordered=False)

    if order.exists():
    	return order[0].orderitems.count()
    else:
    	return 0

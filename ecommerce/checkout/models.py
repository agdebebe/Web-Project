from django.db import models
from django.forms import ModelForm
from django.contrib.auth import get_user_model
# Create your models here.

# Get the user model
User = get_user_model()

# /***************************************************************************************
# *    Title: <MANASCODE>
# *    Author: <Manas Paul>
# *    Date: <21 August 2019>
# *    Code version: <python>
# *    Availability: <https://manascode.com/django-ecommerce-website-tutorial-part-one/>
# *   Edited by: Ablehulu Debebe
# ***************************************************************************************/


# Billing Address Model
class BillingAddress(models.Model):

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	address = models.CharField(max_length=100)
	zipcode = models.CharField(max_length=50)
	city = models.CharField(max_length=30)
	landmark = models.CharField(max_length=20)

	def __str__(self):
		return f'{self.user.username} billing address'

	class Meta:
		verbose_name_plural = "Billing Addresses"

class BillingForm(ModelForm):
	class Meta:
		model = BillingAddress
		fields = ['address', 'zipcode', 'city', 'landmark']

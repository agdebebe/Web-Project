from django.db import models
from django.db.models.signals import pre_save

from .utils import unique_slug_generator


# /***************************************************************************************
# *    Title: <MANASCODE>
# *    Author: <Manas Paul>
# *    Date: <21 August 2019>
# *    Code version: <python>
# *    Availability: <https://manascode.com/django-ecommerce-website-tutorial-part-one/>
# *   Edited by: Ablehulu Debebe
# ***************************************************************************************/

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=300)
    primaryCategory = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class  Product(models.Model):
    mainimage = models.ImageField(upload_to='products/',null=True ,blank=True)
    name = models.CharField(max_length=300)
    slug = models.SlugField(null=True,blank=True)
    categories = models.ManyToManyField(Category)
    preview_text = models.TextField(max_length=200, verbose_name='Preview Text')
    detail_text = models.TextField(max_length=1000, verbose_name='Detail Text')
    price = models.PositiveIntegerField()


    def __str__(self):
        return self.name

def get_product_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(get_product_slug,sender=Product)

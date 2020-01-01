from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


from django.views.generic import ListView
from products.models import Product


class Home(ListView):
    model = Product
    fileds = '__all__'
    template_name = 'products/home.html'


def chat(request):
    if request.method != "POST":
        return HttpResponseRedirect(reverse('index'))
    else:
        title = "Chat Room"
        username = request.POST.get('username')
        return render(request,'chat.html',{"title":title,"username":username})



from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from lazysignup.decorators import allow_lazy_user
from .models import Bag, BagContent
from . import word_generator

# Create your views here.
def index(request):

    return render(request, template_name='bag/index.html')

@allow_lazy_user
def bag_view(request, name):
    b = get_object_or_404(Bag, name=name)
    context = {'bag':b}
    if request.POST.get('add_item'):
        bc = BagContent(bag_content=request.POST.get('bag_item'), bag=b, owner=request.user)
        bc.save()
    elif request.POST.get('pull_item'):
        b.pull_item()

        
    return render(request, 'bag/bag.html', context)

@allow_lazy_user
def new_bag(request):
    name = word_generator.get_words()
    b = Bag(owner=request.user, name=name)
    b.save()

    return redirect('bag', name=name)

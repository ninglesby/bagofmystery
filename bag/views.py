from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Bag, BagContent
from . import word_generator

# Create your views here.
def index(request):

    return HttpResponse(word_generator.get_words())

def bag_view(request, name):
    b = Bag.objects.filter(name=name).first()
    if not b:
        return HttpResponseNotFound()
    else:
        tmp_str = ""
        for x in BagContent.objects.filter(bag=b):
            tmp_str += x.bag_content + "<p/>"
    return HttpResponse(tmp_str)

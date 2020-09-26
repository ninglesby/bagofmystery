from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from lazysignup.decorators import allow_lazy_user
from .models import Bag, BagContent
from .serializers import BagSerializer, BagContentSerializer, BagCounterSerializer
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

@allow_lazy_user
def bag_contents(request, name=None):
    try:
        serializer = BagSerializer(Bag.objects.get(name=name))
    except Bag.DoesNotExist:
        return HttpResponse(status=404)
    return JsonResponse(serializer.data, status=201)

def bag_counter(request, name=None):
    try:
        serializer = BagCounterSerializer(Bag.objects.get(name=name))
    except Bag.DoesNotExist:
        return HttpResponse(status=404)
    return JsonResponse(serializer.data, status=201)

@csrf_exempt
def submit_item(request):
    try:
        bag = Bag.objects.get(name=request.POST['bag_name'])
        content = request.POST['content']
        bag_content = BagContent(owner=request.user, bag=bag, bag_content=content)
        bag_content.save()
    except KeyError:
        return HttpResponse(status=500)

    return HttpResponse(status=200)

@csrf_exempt
def pull_item(request):
    try:
        bag = Bag.objects.get(name=request.POST['bag_name'])
        bag.pull_item()
        bag.save()
    except KeyError:
        return HttpResponse(status=500)
    return HttpResponse(status=200)

@csrf_exempt
def put_item_back(request):
    try:
        bag = Bag.objects.get(name=request.POST['bag_name'])
        bag.put_item_back()
        bag.save()
    except KeyError:
        return HttpResponse(status=500)
    return HttpResponse(status=200)

@csrf_exempt
def discard_item(request):
    try:
        bag = Bag.objects.get(name=request.POST['bag_name'])
        bag.discard_item()
        bag.save()
    except KeyError:
        return HttpResponse(status=500)
    return HttpResponse(status=200)

@csrf_exempt
def empty_bag(request):
    try:
        bag = Bag.objects.get(name=request.POST['bag_name'])
        if request.user == bag.owner:
            bag.empty_bag()
            bag.save()
        else:
            return HttpResponse(status=403)
    except KeyError:
        return HttpResponse(status=500)
    return HttpResponse(status=200)
@csrf_exempt
def restore_items(request):
    try:
        bag = Bag.objects.get(name=request.POST['bag_name'])
        if request.user == bag.owner:
            bag.restore_items()
        else:
            return HttpResponse(status=403)
    except KeyError:
        return HttpResponse(status=500)
    return HttpResponse(status=200)

@csrf_exempt
def delete_bag(request):
    try:
        bag = Bag.objects.get(name=request.POST['bag_name'])
        if request.user == bag.owner:
            bag.delete()
        else:
            return HttpResponse(status=403)
    except KeyError:
        return HttpResponse(status=500)
    return HttpResponse(status=200)


        
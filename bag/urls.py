from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mystery-bag/<slug:name>', views.bag_view, name='bag'),
    path('new_bag', views.new_bag, name='new_bag'),
]
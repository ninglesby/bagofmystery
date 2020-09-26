from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mystery-bag/<slug:name>', views.bag_view, name='bag'),
    path('bag/<slug:name>', views.bag_view, name='bag'),
    path('new_bag', views.new_bag, name='new_bag'),
    path('bag_contents/<slug:name>', views.bag_contents, name='bag_contents'),
    path('submit_item', views.submit_item, name='submit_item'),
    path('pull_item', views.pull_item, name='pull_item'),
    path('put_item_back', views.put_item_back, name='put_item_back'),
    path('discard_item', views.discard_item, name='discard_item'),
    path('empy_bag', views.empty_bag, name='empty_bag'),
    path('restore_items', views.restore_items, name='restore_items'),
    path('delete_Bag', views.delete_bag, name='delete_bag'),
    
]
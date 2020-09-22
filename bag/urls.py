from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:name>', views.bag_view),
]
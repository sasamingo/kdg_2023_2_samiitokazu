
from .views import SweetsView, ListSweetsView, ListTenpoView, DetailSweetView, ItemSweetsView,SyotoSweetView,SfonSweetView,MonSweetView,ChokoSweetView,CzSweetView,BsSweetView,CapSweetView,HuruSweetView
from django.urls import path
from . import views



urlpatterns = [
    path('sweets/index.html', SweetsView.as_view(), name="index_sweets"),
    path('sweets/list',ListSweetsView.as_view(), name='list_sweets'),
    path('sweets/item',ItemSweetsView.as_view(), name='item_sweets'),
    path('sweets/tenpo',ListTenpoView.as_view(), name='tenpo_sweets'),
    path('sweets/details/<int:id>', DetailSweetView.as_view(), name='detail_sweets'),
    path('sweets/syoto',SyotoSweetView.as_view(), name='syoto_sweets'),
    
]





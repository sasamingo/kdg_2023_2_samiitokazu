
from django.contrib.auth import logout
from django.views.generic import ListView
from .models import Sweets
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.


def logout_view(request):
    logout(request)
    return redirect('index_sweets')


class SweetsView(ListView):
    template_name = 'sweets/index.html'
    model = Sweets       
# Create your views here.
class ListSweetsView(ListView):
    template_name = 'sweets/list.html'
    model = Sweets

class ItemSweetsView(ListView):
    template_name = 'sweets/item.html'
    model = Sweets

class ListTenpoView(ListView):
    template_name = 'sweets/tenpo.html'
    model = Sweets

class DetailSweetView(ListView):
    template_name = 'sweets/detail.html'
    model = Sweets

class SyotoSweetView(ListView):
    template_name = 'sweets/syoto.html'
    model = Sweets    

class SfonSweetView(ListView):
    template_name = 'sweets/sfon.html' 
    model = Sweets

class MonSweetView(ListView):
    template_name = 'sweets/mon.html'
    model = Sweets

class ChokoSweetView(ListView):
    template_name = 'sweets/choko.html'
    model = Sweets

class CzSweetView(ListView):
    template_name = 'sweets/cz.html' 
    model = Sweets   

class BsSweetView(ListView):
    template_name = 'sweets/bs.html'
    model = Sweets  

class CapSweetView(ListView):
    template_name = 'sweets/cap.html'
    model = Sweets

class HuruSweetView(ListView):
    template_name = 'sweets/huru.html'
    model = Sweets               


def item_sweets(request):
    # ここにビューロジックを追加する
    return render(request, 'sweets/item.html')




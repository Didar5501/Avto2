
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import mcfcarbrand, mcfcarmodel, mcfcarcolor

class McfCarBrandListView(ListView):
    model = mcfcarbrand
    queryset = mcfcarbrand.objects.all()
    template_name = 'avto_cc/mcfcarbrand_list.html'
    context_object_name = 'ccbrands'

class McfCarModelListView(ListView):
    model = mcfcarmodel
    queryset = mcfcarmodel.objects.all()
    template_name = 'avto_cc/mcfcarmodel_list.html'
    context_object_name = 'ccmodels'

class McfCarColorListView(ListView):
    model = mcfcarcolor
    queryset = mcfcarcolor.objects.all()
    template_name = 'avto_cc/mcfcarcolor_list.html'
    context_object_name = 'cccolors'
# Create your views here.

class CarBrandDetailView(DetailView):
    model = mcfcarbrand
    template_name = 'avto_cc/car_brand_detail.html'
    context_object_name = 'brand'

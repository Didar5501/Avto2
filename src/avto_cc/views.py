from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from .models import mcfcarbrand, mcfcarmodel, mcfcarcolor

class McfCarBrandListView(ListView):
    model = mcfcarbrand
    template_name = 'avto_cc/mcfcarbrand_list.html'
    context_object_name = 'ccbrands'
    paginate_by = 10  

    def get_queryset(self):
        queryset = super().get_queryset()
        name_filter = self.request.GET.get('name_filter') 
        if name_filter:
            queryset = queryset.filter(Name__icontains=name_filter)
        return queryset.select_related('country', 'creationauthor', 'changeauthor')

class McfCarModelListView(ListView):
    model = mcfcarmodel
    template_name = 'avto_cc/mcfcarmodel_list.html'
    context_object_name = 'ccmodels'
    paginate_by = 10  

    def get_queryset(self):
        queryset = super().get_queryset()
        name_filter = self.request.GET.get('name_filter') 
        brand_id = self.request.GET.get('brand_id') 
        if brand_id:
            queryset = queryset.filter(carbrand=brand_id)
        if name_filter:
            queryset = queryset.filter(Name__icontains=name_filter)
        return queryset.select_related('carbrand', 'creationauthor', 'changeauthor')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ccbrands'] = mcfcarbrand.objects.all().select_related('country', 'creationauthor', 'changeauthor')
        return context

class McfCarColorListView(ListView):
    model = mcfcarcolor
    queryset = mcfcarcolor.objects.all()
    template_name = 'avto_cc/mcfcarcolor_list.html'
    context_object_name = 'cccolors'

    def get_queryset(self):
        return super().get_queryset().select_related('creationauthor', 'changeauthor')

class CarBrandDetailView(DetailView):
    model = mcfcarbrand
    template_name = 'avto_cc/car_brand_detail.html'
    context_object_name = 'brand'

    def get_queryset(self):
        return super().get_queryset().select_related('country', 'creationauthor', 'changeauthor')

class CarModelDetailView(DetailView):
    model = mcfcarmodel
    template_name = 'avto_cc/car_model_detail.html'
    context_object_name = 'model'

    def get_queryset(self):
        return super().get_queryset().select_related('carbrand', 'creationauthor', 'changeauthor')


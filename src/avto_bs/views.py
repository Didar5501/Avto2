from django.shortcuts import render
from django.views.generic import ListView
from .models import z_avtobrand, z_avtomodel, z_avtocolor

class ZAvtobrandListView(ListView):
    model = z_avtobrand
    queryset = z_avtobrand.objects.all()
    template_name = 'avto_bs/z_avtobrand_list.html'
    context_object_name = 'brands'

class ZAvtomodelListView(ListView):
    model = z_avtomodel
    queryset = z_avtomodel.objects.all()
    template_name = 'avto_bs/z_avtomodel_list.html'
    context_object_name = 'models'

class ZAvtocolorListView(ListView):
    model = z_avtocolor
    queryset = z_avtocolor.objects.all()
    template_name = 'avto_bs/z_avtocolor_list.html'
    context_object_name = 'colors'
# Create your views here.

from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect
from utils import create_car_brand
from avto_cc.models import country

class CountryListView(ListView):
    model = country
    template_name = 'avto_cc/country_list.html'
    context_object_name = 'countries'

    def get_queryset(self):
        return country.objects.using('cc_db').all()

from avto_cc.models import User


from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from avto_bs.models import z_avtobrand
from avto_cc.models import mcfcarbrand
from avto_cc.models import User, country
from utils import create_car_brand, update_car_brand

class CreateCarBrandView(CreateView):
    model = mcfcarbrand
    template_name = 'avto_bs/create_car_brand.html'
    fields = ['Name', 'country']

    def form_valid(self, form):
        creationauthor = User.objects.using('cc_db').get(id=3)

        country_id = form.cleaned_data['country']
        country_obj = country.objects.using('cc_db').get(id=country_id)

        avto_brand, cc_brand = create_car_brand(form.cleaned_data['Name'], country_obj, creationauthor)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('mcfcarbrand_list')



class EditCarBrandView(UpdateView):
    model = mcfcarbrand
    template_name = 'avto_bs/edit_car_brand.html'
    fields = ['Name', 'country']
    success_url = reverse_lazy('mcfcarbrand_list')

    def form_valid(self, form):
        changeauthor = User.objects.using('cc_db').get(id=3)
        update_car_brand(self.kwargs['pk'], form.cleaned_data['Name'], form.cleaned_data['country'])
        return super().form_valid(form)

from django.urls import reverse_lazy
from django.views.generic import DeleteView
from avto_bs.models import z_avtobrand
from avto_cc.models import mcfcarbrand
from utils import delete_car_brand

class DeleteCarBrandView(DeleteView):
    model = mcfcarbrand
    success_url = reverse_lazy('mcfcarbrand_list')
    template_name = 'avto_bs/delete_car_brand_confirm.html'  # Шаблон для подтверждения удаления

    def delete(self, request, *args, **kwargs):
        brand = self.get_object()
        idbs = brand.idbs
        delete_car_brand(idbs)
        return super().delete(request, *args, **kwargs)
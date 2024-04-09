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


from avto_cc.models import country
from avto_cc.models import User
from utils import create_car_brand, update_car_brand

class CountryListView(ListView):
    model = country
    template_name = 'avto_cc/country_list.html'
    context_object_name = 'countries'

    def get_queryset(self):
        return country.objects.using('cc_db').all()


from avto_cc.models import mcfcarbrand, mcfcarmodel
from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import View


class CreateCarBrandView(View):
    template_name = 'avto_bs/create_car_brand.html'
    
    def get(self, request, *args, **kwargs):
        countries = country.objects.using('cc_db').all()
        return render(request, self.template_name, {'countries': countries})

    def post(self, request, *args, **kwargs):
        brand_name = request.POST.get('brand_name')
        country_id = request.POST.get('country')
        
        country_obj = country.objects.using('cc_db').get(id=country_id)
        
        creationauthor = User.objects.using('cc_db').get(id=3)
        
        avto_brand, cc_brand = create_car_brand(brand_name, country_obj, creationauthor)
        
        return self.form_valid(request, avto_brand, cc_brand)

    def form_valid(self, request, avto_brand, cc_brand):
        return HttpResponse("Бренд автомобиля успешно создан в обеих базах данных.")



from django.views.generic import UpdateView

class EditCarBrandView(UpdateView):
    model = mcfcarbrand
    template_name = 'avto_bs/edit_car_brand.html'
    fields = ['Name', 'country']
    success_url = reverse_lazy('mcfcarbrand_list')

    def form_valid(self, form):
        changeauthor = User.objects.using('cc_db').get(id=3)
        update_car_brand(self.kwargs['pk'], form.cleaned_data['Name'], form.cleaned_data['country'])
        return super().form_valid(form)



from django.views.generic import DeleteView
from utils import delete_car_brand

from django.views.generic import DeleteView
from utils import delete_car_brand

class DeleteCarBrandView(DeleteView):
    model = mcfcarbrand
    success_url = reverse_lazy('mcfcarbrand_list')
    template_name = 'avto_bs/delete_car_brand_confirm.html' 

    def get(self, request, *args, **kwargs):
        brand = self.get_object()
        idbs = brand.idbs
        print("IDBS before deletion:", idbs)
        return super().get(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        brand = self.get_object()
        idbs = brand.idbs
        delete_car_brand(idbs)
        return super().delete(request, *args, **kwargs)



from utils import create_car_model, update_car_model

class CreateCarModelView(View):
    template_name = 'avto_bs/create_car_model.html'
    
    def get(self, request, *args, **kwargs):
        brands = mcfcarbrand.objects.using('cc_db').all()
        return render(request, self.template_name, {'brands': brands})

    def post(self, request, *args, **kwargs):
        model_name = request.POST.get('model_name')
        brand_id = request.POST.get('brand')
        
        brand_obj = mcfcarbrand.objects.using('cc_db').get(id=brand_id)
        
        creationauthor = User.objects.using('cc_db').get(id=3)
        
        avto_model, cc_model = create_car_model(model_name, brand_obj, creationauthor)
        
        return self.form_valid(request, avto_model, cc_model)

    def form_valid(self, request, avto_model, cc_model):
        return HttpResponse("Модель автомобиля успешно создана в обеих базах данных.")

class EditCarModelView(UpdateView):
    model = mcfcarmodel
    template_name = 'avto_bs/edit_car_model.html'
    fields = ['Name', 'carbrand']
    success_url = reverse_lazy('mcfcarmodel_list')

    def form_valid(self, form):
        changeauthor = User.objects.using('cc_db').get(id=3)
        update_car_model(self.kwargs['pk'], form.cleaned_data['Name'], form.cleaned_data['carbrand'])
        return super().form_valid(form)
from django.views.generic import ListView
from .models import z_avtobrand, z_avtomodel, z_avtocolor

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

from django.views.decorators.cache import cache_page

class CreateCarBrandView(View):
    template_name = 'avto_bs/create_car_brand.html'
    
    @cache_page(60 * 15)  # Кэшировать на 15 минут
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
# class CreateCarBrandView(View):
#     template_name = 'avto_bs/create_car_brand.html'
    
#     def get(self, request, *args, **kwargs):
#         countries = country.objects.using('cc_db').all()
#         return render(request, self.template_name, {'countries': countries})

#     def post(self, request, *args, **kwargs):
#         brand_name = request.POST.get('brand_name')
#         country_id = request.POST.get('country')
        
#         country_obj = country.objects.using('cc_db').get(id=country_id)
        
#         creationauthor = User.objects.using('cc_db').get(id=3)
        
#         avto_brand, cc_brand = create_car_brand(brand_name, country_obj, creationauthor)
        
#         return self.form_valid(request, avto_brand, cc_brand)

#     def form_valid(self, request, avto_brand, cc_brand):
#         return HttpResponse("Бренд автомобиля успешно создан в обеих базах данных.")



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


from django.shortcuts import redirect
from django.views.generic import View
from avto_cc.models import mcfcarbrand

class DeleteCarBrandView(View):
    def post(self, request, pk):
        brand = mcfcarbrand.objects.get(pk=pk)
        avto_brand = brand.get_z_avtobrand()
        avto_brand.delete()
        brand.delete()
        return redirect('mcfcarbrand_list')


from django.shortcuts import render, redirect
from django.views import View
from .models import z_avtobrand, z_avtomodel
from avto_cc.models import mcfcarmodel, mcfcarbrand
from django.http import HttpResponse
from django.utils import timezone

class CreateCarModelView(View):
    template_name = 'avto_bs/create_car_model.html'

    def get(self, request):
        brands = z_avtobrand.objects.all()
        return render(request, self.template_name, {'brands': brands})

    def post(self, request):
        name = request.POST.get('model_name')
        brand_id = request.POST.get('brand')

        try:
            z_brand = z_avtobrand.objects.get(BrandID=brand_id)
            z_model = z_avtomodel.objects.create(Name=name, BrandID=z_brand)

            mcf_brand = mcfcarbrand.objects.get(idbs=brand_id).id

            mcf_model= mcfcarmodel.objects.create(
                Name=name,
                carbrand_id=mcf_brand,
                idbs=z_model.ModelID,
                creationdate=timezone.now(),
                changedate=timezone.now(),
                mcfcode=0,  
                changeauthor_id=3, 
                creationauthor_id=3  
            )

            new_mcfcode = str(mcf_model.id)
            mcfcarmodel.objects.filter(idbs=z_model.ModelID).update(mcfcode=new_mcfcode)


            return redirect('mcfcarmodel_list')
        except z_avtobrand.DoesNotExist:
            return HttpResponse("Brand does not exist")

from django.shortcuts import render, redirect
from django.views import View
from django.utils import timezone
from .models import z_avtomodel, z_avtobrand
from avto_cc.models import mcfcarmodel, mcfcarbrand

class EditCarModelView(View):
    template_name = 'avto_bs/edit_car_model.html'

    def get(self, request, model_id):  
        model_instance = z_avtomodel.objects.get(ModelID=model_id)
        brands = z_avtobrand.objects.all()
        return render(request, self.template_name, {'model_instance': model_instance, 'brands': brands})

    def post(self, request, model_id):  
        name = request.POST.get('model_name')
        brand_id = request.POST.get('brand')

        try:
            z_brand = z_avtobrand.objects.get(BrandID=brand_id)
            z_model = z_avtomodel.objects.get(ModelID=model_id)

            mcf_brand = mcfcarbrand.objects.get(idbs=brand_id).id

            mcfcarmodel.objects.filter(idbs=z_model.ModelID).update(
                Name=name,
                carbrand_id=mcf_brand,
                changedate=timezone.now(),
                changeauthor_id=3  
            )

            return redirect('mcfcarmodel_list')
        except z_avtobrand.DoesNotExist:
            return HttpResponse("Brand does not exist")
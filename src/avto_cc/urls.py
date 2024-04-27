from django.urls import path
from .views import McfCarBrandListView, McfCarModelListView, McfCarColorListView, CarBrandDetailView, CarModelDetailView
from avto_bs.views import DeleteCarBrandView


urlpatterns = [
    path('mcfcarbrands/', McfCarBrandListView.as_view(), name='mcfcarbrand_list'),
    path('mcfcarmodels/', McfCarModelListView.as_view(), name='mcfcarmodel_list'),
    path('mcfcarcolors/', McfCarColorListView.as_view(), name='mcfcarcolor_list'),
    path('car_brand_detail/<int:pk>/', CarBrandDetailView.as_view(), name='car_brand_detail'),
    path('car_model_detail/<int:pk>/', CarModelDetailView.as_view(), name='car_model_detail'),
   


]
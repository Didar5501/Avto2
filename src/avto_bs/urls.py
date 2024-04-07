from django.urls import path
from .views import ZAvtobrandListView, ZAvtomodelListView, ZAvtocolorListView
from .views import CreateCarBrandView, EditCarBrandView, DeleteCarBrandView
from .views import CountryListView

urlpatterns = [
    path('z_avtobrands/', ZAvtobrandListView.as_view(), name='z_avtobrand_list'),
    path('z_avtomodels/', ZAvtomodelListView.as_view(), name='z_avtomodel_list'),
    path('z_avtocolors/', ZAvtocolorListView.as_view(), name='z_avtocolor_list'),
    path('create_car_brand/', CreateCarBrandView.as_view(), name='create_car_brand'),
    path('edit_car_brand/<int:pk>/',EditCarBrandView.as_view(), name='edit_car_brand'),
    path('delete/<int:pk>/', DeleteCarBrandView.as_view(), name='delete_car_brand'),
    path('countries/', CountryListView.as_view(), name='country_list'),
]
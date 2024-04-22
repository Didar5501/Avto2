from django.urls import path
from .views import CreateCarBrandView, EditCarBrandView, DeleteCarBrandView
from .views import CreateCarModelView, EditCarModelView
from .views import CountryListView

urlpatterns = [
    path('create_car_brand/', CreateCarBrandView.as_view(), name='create_car_brand'),
    path('edit_car_brand/<int:pk>/',EditCarBrandView.as_view(), name='edit_car_brand'),
    path('delete_car_brand/<int:pk>/', DeleteCarBrandView.as_view(), name='delete_car_brand'),
    path('countries/', CountryListView.as_view(), name='country_list'),
    path('create_car_model/', CreateCarModelView.as_view(), name='create_car_model'),
    path('edit_car_model/<int:pk>/', EditCarModelView.as_view(), name='edit_car_model'),
]
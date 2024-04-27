from django.urls import path, re_path
from . import views 

urlpatterns = [
    path('create_mcfcarbrand/', views.McfCarBrandCreateView.as_view(), name='mcfcarbrand-create'),
    path('detail_mcfcarbrand/<int:id>/', views.McfCarBrandDetailView.as_view(), name='mcfcarbrand-detail'),

    path('create_z_avtobrand/', views.ZAvtobrandCreateView.as_view(), name='create_z_avtobrand'),
    path('detail_z_avtobrand/<int:BrandID>/', views.ZAvtobrandDetailAPIView.as_view(), name='update_z_avtobrand'),
    
    path('z_avtomodels/', views.ZAvtomodelListAPIView.as_view(), name='z_avtomodel-list'),

    path('weather/', views.WeatherAPIView.as_view(), name='weather'),

]
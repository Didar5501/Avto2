from django.urls import path, re_path
from . import views 

urlpatterns = [
    path('create_mcfcarbrand/', views.McfCarBrandCreateView.as_view(), name='mcfcarbrand-create'),

    path('create_z_avtobrand/', views.ZAvtobrandCreateView.as_view(), name='create_z_avtobrand'),
    path('update_z_avtobrand/<int:BrandID>/', views.ZAvtobrandDetailAPIView.as_view(), name='update_z_avtobrand'),
    path('delete_z_avtobrand/<int:BrandID>/', views.ZAvtobrandDeleteView.as_view(), name='delete_z_avtobrand'),
    
    path('z_avtomodels/', views.ZAvtomodelListAPIView.as_view(), name='z_avtomodel-list'),


]
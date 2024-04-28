from rest_framework import generics
from .serializers import McfCarBrandCreateSerializer, McfCarBrandSerializer
from avto_cc.models import mcfcarbrand

class McfCarBrandCreateView(generics.CreateAPIView): #Создание в таблице mcfcarbrand
    queryset = mcfcarbrand.objects.all()
    serializer_class = McfCarBrandCreateSerializer

class McfCarBrandDetailView(generics.RetrieveUpdateDestroyAPIView):   #Получение деталки, обновение, удаление
    queryset = mcfcarbrand.objects.all()
    serializer_class = McfCarBrandSerializer
    lookup_field = 'id'




from rest_framework import status
from avto_bs.models import z_avtobrand
from .serializers import ZAvtobrandCreateSerializer, ZAvtobrandSerializer

class ZAvtobrandCreateView(generics.CreateAPIView): #Создание в таблице z_avtobrand
    queryset = z_avtobrand.objects.all()
    serializer_class = ZAvtobrandCreateSerializer


class ZAvtobrandDetailAPIView(generics.RetrieveUpdateDestroyAPIView):  #Получение деталки, обновение, удаление
    queryset = z_avtobrand.objects.all()
    serializer_class = ZAvtobrandSerializer
    lookup_field = 'BrandID'


from avto_bs.models import z_avtomodel
from .serializers import ZAvtomodelSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class ZAvtomodelListAPIView(generics.ListCreateAPIView):
    serializer_class = ZAvtomodelSerializer
    queryset = z_avtomodel.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter,  DjangoFilterBackend ]
    filterset_fields = ['BrandID', 'ModelID']
    search_fields = ['Name']  
    ordering_fields = ['BrandID']




import requests
from django.views.generic import View
from django.http import JsonResponse

class WeatherAPIView(View):
    def get(self, request, *args, **kwargs):
        user=request.user
        url = "https://weatherbit-v1-mashape.p.rapidapi.com/current"
        querystring = {"lon": "43.23269713756249", "lat": "76.91163003444672", "lang": "ru"}
        headers = {
            "X-RapidAPI-Key": "fbdebfb574msh392cfcd133e5ea6p148281jsne746d5653e9d",
            "X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        weather_data = response.json()
        
        return JsonResponse(weather_data)
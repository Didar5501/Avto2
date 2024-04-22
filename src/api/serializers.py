from rest_framework import serializers
from avto_cc.models import mcfcarbrand, country, User
from django.utils import timezone

class McfCarBrandCreateSerializer(serializers.ModelSerializer):
    creationauthor = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    creationdate = serializers.DateTimeField(default=timezone.now)
    country = serializers.PrimaryKeyRelatedField(queryset=country.objects.all())

    class Meta:
        model = mcfcarbrand
        fields = ['Name', 'idbs', 'country', 'mcfcode', 'creationauthor', 'creationdate']

    def create(self, validated_data):
        mcf_car_brand = super().create(validated_data)
        mcf_car_brand.mcfcode = mcf_car_brand.id
        mcf_car_brand.save()
        return mcf_car_brand





from rest_framework import serializers
from avto_bs.models import z_avtobrand

class ZAvtobrandCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = z_avtobrand
        fields = ['Name']

from rest_framework import serializers
from avto_bs.models import z_avtobrand

class ZAvtobrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = z_avtobrand
        fields = '__all__'





from rest_framework import serializers
from avto_bs.models import z_avtomodel

class ZAvtomodelSerializer(serializers.ModelSerializer):
    class Meta:
        model = z_avtomodel
        fields = ['ModelID', 'Name', 'BrandID']



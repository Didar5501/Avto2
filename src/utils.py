from django.db import transaction
from avto_bs.models import z_avtobrand
from avto_cc.models import mcfcarbrand
from datetime import date

def create_car_brand(name, country, creationauthor):
    with transaction.atomic():
        avto_brand = z_avtobrand(Name=name)
        avto_brand.save()
        today = date.today()
        cc_brand = mcfcarbrand(Name=name, country=country,idbs=avto_brand.BrandID,creationauthor=creationauthor,creationdate=today, changeauthor=creationauthor, changedate=today)
        cc_brand.save()
        cc_brand.mcfcode = str(cc_brand.id)
        cc_brand.save()
    return avto_brand, cc_brand

def update_car_brand(brand_id, new_name, new_country_name):
    brand = mcfcarbrand.objects.using('cc_db').get(id=brand_id)
    brand.Name = new_name
    today = date.today()
    brand.changedate = today
    brand.save()
    avto_brand = z_avtobrand.objects.get(BrandID=brand.idbs)
    avto_brand.Name = new_name
    avto_brand.changedate = today
    avto_brand.save()
    return brand, avto_brand


def delete_car_brand(idbs):
    cc_brand = mcfcarbrand.objects.using('cc_db').get(idbs=idbs)
    
    try:
        avto_brand = z_avtobrand.objects.using('avto_db').get(BrandID=idbs)
        avto_brand.delete()
    except z_avtobrand.DoesNotExist:
        pass
    cc_brand.delete()

from avto_bs.models import z_avtomodel
from avto_cc.models import mcfcarmodel

def create_car_model(name, brand, creationauthor):
    with transaction.atomic():
        avto_model = z_avtomodel(Name=name, BrandID=brand)
        avto_model.save()
        today = date.today()
        cc_model = mcfcarmodel(Name=name, carbrand=brand, idbs=avto_model.ModelID,
                               creationauthor=creationauthor, creationdate=today,
                               changeauthor=creationauthor, changedate=today)
        cc_model.save()
        cc_model.mcfcode = str(cc_model.id)
        cc_model.save()
    return avto_model, cc_model

def update_car_model(model_id, new_name, new_brand):
    model = mcfcarmodel.objects.using('cc_db').get(id=model_id)
    model.Name = new_name
    today = date.today()
    model.changedate = today
    model.save()
    avto_model = z_avtomodel.objects.get(ModelID=model.idbs)
    avto_model.Name = new_name
    avto_model.changedate = today
    avto_model.save()
    return model, avto_model
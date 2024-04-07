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


from avto_bs.models import z_avtobrand
from avto_cc.models import mcfcarbrand

def delete_car_brand(idbs):
    # Находим бренд в avto_db по idbs
    avto_brand = z_avtobrand.objects.get(BrandID=idbs)
    
    # Находим бренд в cc_db по idbs
    cc_brand = mcfcarbrand.objects.get(idbs=idbs)
    
    # Удаляем бренд из обеих баз данных
    avto_brand.delete()
    cc_brand.delete()
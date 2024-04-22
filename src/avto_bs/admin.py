from django.contrib import admin
from .models import z_avtobrand, z_avtomodel

@admin.register(z_avtobrand)
class z_avtobrandAdmin(admin.ModelAdmin):
    list_display=['BrandID',
                    'Name']


@admin.register(z_avtomodel)
class z_avtomodelAdmin(admin.ModelAdmin):
    list_display=['ModelID','BrandID','Name']
   

   
# Register your models here.

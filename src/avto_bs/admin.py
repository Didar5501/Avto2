from django.contrib import admin
from .models import z_avtobrand

@admin.register(z_avtobrand)
class z_avtobrandAdmin(admin.ModelAdmin):
    list_display=['BrandID',
                    'Name']
   

   
# Register your models here.

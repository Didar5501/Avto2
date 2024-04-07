from django.contrib import admin
from .models import mcfcarbrand

@admin.register(mcfcarbrand)
class McfcarbrandAdmin(admin.ModelAdmin):
    list_display=[ 
                    'id', 
                    'uid', 
                    'Name',
                    'idbs', 
                    'country' ,
                    'creationdate' ,
                    'creationauthor' ,
                    'changedate' ,
                    'changeauthor' ,
                    'mcfcode',
                ]
    readonly_fields=[
                     'creationdate',
                     'changedate'

                ]
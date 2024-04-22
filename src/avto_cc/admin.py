from django.contrib import admin
from .models import mcfcarbrand, mcfcarmodel, country, User

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

@admin.register(mcfcarmodel)
class McfcarmodelAdmin(admin.ModelAdmin):
    list_display=[ 
                    'id', 
                    'uid', 
                    'Name',
                    'carbrand',
                    'idbs', 
                    'mcfcode',
                    'creationdate' ,
                    'creationauthor' ,
                    'changedate' ,
                    'changeauthor' ,
                   
                ]
    readonly_fields=[
                     'creationdate',
                     'changedate'

                ]


@admin.register(country)
class Country(admin.ModelAdmin):
    list_display=[ 
                    'id',  
                    'Name'
                   
                ]


@admin.register(User)
class User(admin.ModelAdmin):
    list_display= ['id',
                  'username'
    ]
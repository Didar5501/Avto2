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
    ordering = [ 
                'creationdate',
                ]
    list_filter=[
        'country',
        'creationauthor' ,
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

    ordering = [ 
                'creationdate',
                ]

    list_filter=[
                'carbrand',
                'creationauthor' ,
    ]

    list_per_page=5

    list_editable=['Name','carbrand',]

    search_fields=['Name', 'idbs']



    date_hierarchy='creationdate'
    

@admin.register(country)
class Country(admin.ModelAdmin):
    list_display=[ 
                    'id',  
                    'Name'
                   
                ]



from avto_cc.models import mcfcarbrand

class UserInline(admin.StackedInline):
    model = mcfcarbrand
    extra = 3
    fk_name = 'creationauthor'


@admin.register(User)
class User(admin.ModelAdmin):
    list_display= ['id',
                  'username'
    ]

    inlines=[UserInline]

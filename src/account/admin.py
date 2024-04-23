from django.contrib import admin
from . import models

@admin.register(models.User)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        'email',
        'first_name',
        'last_name',
        "mobile_phone",
        "date_joined",
        "position",
    ]
    readonly_fields = ["password",]
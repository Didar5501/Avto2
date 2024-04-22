from django.contrib import admin
from . import models

@admin.register(models.User)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        'email',
        "mobile_phone",
        "date_joined"
    ]
    readonly_fields = ["password",]
from django.contrib import admin

from app_admon.models import *
# Register your models here.

class ClienteEnAmind(admin.ModelAdmin):
    list_display = ("id", "nombre")

admin.site.register(Cliente, ClienteEnAmind)


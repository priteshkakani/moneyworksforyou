from django.contrib import admin
from .models import Stock


# Register your models here.

class StockAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "price",)


admin.site.register(Stock, StockAdmin)

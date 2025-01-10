from django.contrib import admin
from .models import Coffee

# Register your models here.
# admin.site.register(Coffee)

@admin.register(Coffee)
class CoffeeAdmin(admin.ModelAdmin):
    list_display = ('coffee_name', 'vendor', 'listing_approved')
    search_fields = ['title', 'vendor']
    list_filter = ('vendor', 'listing_approved')
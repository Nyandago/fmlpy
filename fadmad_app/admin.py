from django.contrib import admin
from .models import Bidhaa



# admin.site.register(Bidhaa)


@admin.register(Bidhaa)
class BidhaaAdmin(admin.ModelAdmin):
    list_display = ('bidhaa_jina','bidhaa_shipping_cost','bidhaa_shipping_days','bidhaa_published','bidhaa_country',)
    ordering = ('bidhaa_jina',)
    search_fields = ('bidhaa_jina','bidhaa_country',)

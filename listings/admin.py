from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.

from .models import Listing as Programs

# class ListingAdmin(ImportExportModelAdmin):
#     pass


class ListingAdmin(ImportExportModelAdmin):
    list_display = ('id','programname','programtype','address','amount','is_published')
    list_display_links = ('id','programname')
    list_filter = ('state',)
    list_editable = ('is_published',)
    search_fields = ('programname','address','programoriginator','city','amountofassistance')
    list_per_page = 25

admin.site.register(Programs,ListingAdmin)


from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.

from .models import Listing

# class ListingAdmin(ImportExportModelAdmin):
#     pass


class ListingAdmin(ImportExportModelAdmin):
    list_display = ('id','title','program','address','amount','is_published')
    list_display_links = ('id','title')
    list_filter = ('state',)
    list_editable = ('is_published',)
    search_fields = ('title','address','program','city')
    list_per_page = 25

admin.site.register(Listing,ListingAdmin)


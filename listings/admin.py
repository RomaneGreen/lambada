from django.contrib import admin

# Register your models here.

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','title','program','address','amount','is_published')
    list_display_links = ('id','title')
    list_filter = ('state',)
    list_editable = ('is_published',)
    search_fields = ('title','address','program','city')
    list_per_page = 25

admin.site.register(Listing,ListingAdmin)
from django.contrib import admin

# Register your models here.

from .models import Lender


class LenderAdmin(admin.ModelAdmin):
    list_display = ('id','name','location','phone')
    list_display_links = ('id','name')
    list_filter = ('name',)
    search_fields = ('id','name','location','phone')
    list_per_page = 25


admin.site.register(Lender,LenderAdmin)
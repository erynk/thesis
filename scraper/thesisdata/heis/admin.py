from django.contrib import admin
from .models import Region, City, Institution, Page
# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_display = (
        'institution', 
        'title', 
        'web_address', 
        'home_page')

class PageInline(admin.TabularInline):
    model = Page

class InstitutionAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'city', 
        'get_region',
        'public', 
        'non_profit', 
        'university', 
        'community_college', 
        'votech')
    inlines = [PageInline, ]

    def get_region(self, obj):
        return obj.city.region
        
    get_region.admin_order_field  = 'region'  #Allows column order sorting
    get_region.short_description = 'Region'  #Renames column head

class CityAdmin(admin.ModelAdmin):
    list_display = ('city', 'region')

admin.site.register(Region)
admin.site.register(City, CityAdmin)
admin.site.register(Institution, InstitutionAdmin)
admin.site.register(Page, PageAdmin)

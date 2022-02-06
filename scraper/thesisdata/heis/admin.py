from django.contrib import admin
from .models import Region, City, Institution, Page
# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'web_address')


admin.site.register(Region)
admin.site.register(City)
admin.site.register(Institution)
admin.site.register(Page, PageAdmin)

from django.contrib import admin
from .models import Principle, Guideline, Criterion

# Register your models here.

class GuidelineInline(admin.TabularInline):
    model = Guideline
    extra = 0

class CriterionInline(admin.TabularInline):
    model = Criterion
    extra = 0

class PrincipleAdmin(admin.ModelAdmin):
    inlines = [GuidelineInline, ]

class GuidelineAdmin(admin.ModelAdmin):
    inlines = [CriterionInline, ]
    
admin.site.register(Principle, PrincipleAdmin)
admin.site.register(Guideline, GuidelineAdmin)
admin.site.register(Criterion)

from django.contrib import admin
from .models import ReviewPage, Tool, Failure, ReviewAutomated

# Register your models here.

class FailureInline(admin.TabularInline):
    model = Failure

class ReviewPageInline(admin.TabularInline):
    model = ReviewPage

class ReviewPageAdmin(admin.ModelAdmin):
    inlines = [FailureInline, ]

class ReviewAutomatedAdmin(admin.ModelAdmin):
    inlines = [ReviewPageInline, ]


admin.site.register(Tool)
admin.site.register(Failure)
admin.site.register(ReviewPage, ReviewPageAdmin)
admin.site.register(ReviewAutomated)

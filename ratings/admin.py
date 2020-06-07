from django.contrib import admin

from . models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['pk', 'review', 'updated']
    list_display_links = ['review', ]


admin.site.register(Review, ReviewAdmin)

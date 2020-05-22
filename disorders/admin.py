from django.contrib import admin

from . models import Disorder, Symptom


class DisorderAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'verified', 'updated']
    list_display_links = ['title', ]


class SymptomAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created']
    list_display_links = ['title', ]


admin.site.register(Disorder, DisorderAdmin)
admin.site.register(Symptom, SymptomAdmin)

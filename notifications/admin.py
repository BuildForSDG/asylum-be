from django.contrib import admin

from . models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ['pk', 'subject', 'sender', 'timestamp', 'mail_sent']
    list_display_links = ['subject', ]


admin.site.register(Message, MessageAdmin)

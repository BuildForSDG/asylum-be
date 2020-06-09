from django.contrib import admin

from . models import Invitation, Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ['pk', 'subject', 'sender', 'timestamp', 'mail_sent']
    list_display_links = ['subject', ]


class InvitationAdmin(admin.ModelAdmin):
    list_display = ['pk', 'recipient', 'mail_sent', 'accepted', 'timestamp']
    list_display_links = ['recipient', ]


admin.site.register(Message, MessageAdmin)
admin.site.register(Invitation, InvitationAdmin)

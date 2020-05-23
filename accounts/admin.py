from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . models import User, Profile


class CustomUserAdmin(UserAdmin):
    pass


class ProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)

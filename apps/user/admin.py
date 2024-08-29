from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from apps.user.models import User
from django.contrib import admin
from django.contrib.auth.models import Group

# Unregister the Group model from the admin site:
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass

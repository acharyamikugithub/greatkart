from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class AccountAdmin(UserAdmin):
    list_display=['username','first_name','last_name','email','date_joined','last_login','is_active']
    list_display_links=['email','first_name','last_name','username']
    readonly_fields=['last_login','date_joined']
    ordering=('-date_joined',)
    filter_horizontal=()
    list_filter=()
    fieldsets=()
admin.site.register(Account,AccountAdmin)

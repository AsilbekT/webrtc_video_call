from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account, MobileUser, MobileToken


class AccountAdmin(UserAdmin):
    list_display = ('phone_number', 'username', 'date_joined',
                    'last_login', 'is_admin', 'is_staff')
    search_fields = ('phone_number', 'username',)
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class MobileUserAdmin(UserAdmin):
    list_display = ('phone_number', 'username', 'is_active')
    search_fields = ('phone_number', 'username', 'is_active')
    readonly_fields = ()

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
admin.site.register(MobileUser, MobileUserAdmin)
admin.site.register(MobileToken)

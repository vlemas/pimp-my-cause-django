from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from custom_user.admin import EmailUserAdmin

from .models import PimpUser, CauseProfile, MarketerProfile, Qualification


class PimpUserAdmin(EmailUserAdmin):

    fieldsets = (
        (None, {'fields': ('email', 'password', 'linkedin', 'twitter', 'name',
                'surname', 'phone', 'country', 'city', 'postcode', 'position',
                'usertype', 'bio', 'website', 'image', 'featured')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                                    'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

# Register your models here.
admin.site.register(PimpUser, PimpUserAdmin)
admin.site.register(MarketerProfile)
admin.site.register(CauseProfile)
admin.site.register(Qualification)

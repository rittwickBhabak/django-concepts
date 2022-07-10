from django.contrib import admin
from django.forms import Textarea
from .models import NewUser 
from django.contrib.auth.admin import UserAdmin 

class UserAdminConfig(UserAdmin):
    search_fields = ('email', 'user_name', 'first_name')
    list_filter = ('email', 'user_name', 'first_name', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('email', 'user_name', 'first_name', 'is_active', 'is_staff')

    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('about', )}),
    )

    formfield_overrides = {
        NewUser.about: {'widget': Textarea(attrs={'rows': 5, 'cols': 40})},
    }

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'password1', 'password2', 'is_staff', 'is_active')
            }
        ),
    )
    
admin.site.register(NewUser, UserAdminConfig)
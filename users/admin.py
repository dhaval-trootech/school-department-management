from django.contrib import admin
from .models import SchoolUser


# Register your models here.
@admin.register(SchoolUser)
class SchoolUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'email', 'user_type', 'user_icon')
    actions = ['ban_users']

    # USER BANNING FUNCTION
    def ban_users(self, request, queryset):
        queryset.update(is_active=False)

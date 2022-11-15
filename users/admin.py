from django.contrib import admin
from .models import SchoolUser


# Register your models here.
@admin.register(SchoolUser)
class SchoolUSerAdmin(admin.ModelAdmin):
    pass

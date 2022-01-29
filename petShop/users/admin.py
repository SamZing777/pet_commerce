from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
	list_display = ['username', 'is_seller', 'is_vetenary_doctor']


admin.site.register(User, UserAdmin)


"""
Admin
PetAdmin123
"""

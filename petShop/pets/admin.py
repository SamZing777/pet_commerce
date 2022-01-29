from django.contrib import admin

from .models import (
	Animal,
	SubCategory,
	Pet
	)


class SubCategoryInline(admin.StackedInline):
	model = SubCategory
	extra = 1


class AnimalAdmin(admin.ModelAdmin):
	list_display = ['name', 'is_active']
	search_fields = ['name']
	list_display_links = ['name']
	list_per_page = 20
	pre_populated_fields = {'slug': ('name')}
	inlines = [SubCategoryInline,]


class PetAdmin(admin.ModelAdmin):
	list_display = ['name', 'old_price', 'price']
	search_fields = ['name']
	list_display_links = ['name']
	list_per_page = 20
	pre_populated_fields = {'slug': ('name')}


admin.site.register(Animal, AnimalAdmin)
admin.site.register(Pet, PetAdmin)

from django.contrib import admin
from .models import Tour
from .models import Category

class TourAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name', 'date', 'equipment', 'country')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'equipment')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Tour, TourAdmin)
admin.site.register(Category, CategoryAdmin)
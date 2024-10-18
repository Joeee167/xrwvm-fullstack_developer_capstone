from django.contrib import admin
from .models import CarMake, CarModel

# Inline class for CarModel
class CarModelInline(admin.TabularInline):  
    model = CarModel
    extra = 1  

# Admin class for CarModel
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'car_type', 'year', 'dealer_id', 'color')
    list_filter = ('car_type', 'year', 'car_make')
    search_fields = ('name', 'car_make__name')

# Admin class for CarMake
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'founded_year', 'country')
    search_fields = ('name', 'country')
    inlines = [CarModelInline]  

# Register models with their respective admins
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)

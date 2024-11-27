from django.contrib import admin
from .models import Business, Category, Service

class ServiceInline(admin.TabularInline):
    model = Service
    extra = 1  
    fields = ['name', 'price']

class BusinessAdmin(admin.ModelAdmin):
    inlines = [ServiceInline]  
    list_display = ('name', 'description', 'phone_number', 'email', 'address') 

admin.site.register(Business, BusinessAdmin)
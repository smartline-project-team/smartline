from django.contrib import admin
from .models import Business, Category, Service, Specialist

class SpecialistInline(admin.TabularInline):
    model = Specialist
    extra = 1
    fields = ['first_name', 'last_name']

class BusinessAdmin(admin.ModelAdmin):
    inlines = [SpecialistInline]
    list_display = ('name', 'description', 'phone_number', 'email', 'address')

admin.site.register(Business, BusinessAdmin)
admin.site.register(Category)
admin.site.register(Service)
admin.site.register(Specialist)
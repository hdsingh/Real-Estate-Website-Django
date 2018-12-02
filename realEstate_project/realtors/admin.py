from django.contrib import admin

# Register your models here.
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('name','is_mvp','email','hire_date')
    list_display_links = ('name','email')
    list_per_page = 10
    search_fields = ('name',)
    list_editable = ('is_mvp',)

admin.site.register(Realtor,RealtorAdmin)
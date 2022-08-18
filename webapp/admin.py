from django.contrib import admin
from .models import *

class ServiceAdmin(admin.ModelAdmin):
	list_display = ['title']

class PortfolioAdmin(admin.ModelAdmin):
	list_display = ['name','tagline']

class ContactAdmin(admin.ModelAdmin):
	list_display = ['email', 'message', 'created_date']

admin.site.register(Service, ServiceAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Contact, ContactAdmin)
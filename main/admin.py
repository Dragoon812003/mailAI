from django.contrib import admin
from .models import *

admin.site.site_header = "Mail AI Admin"
admin.site.site_title = "Mail AI Admin Panel"
admin.site.index_title = "Welcome to Mail AI's Admin Panel!"

class DeveloperAdmin(admin.ModelAdmin):
    exclude = ('timestamp',)  # Exclude the timestamp field from the admin form

# Register the Developer model with the custom admin class
admin.site.register(Developer, DeveloperAdmin)

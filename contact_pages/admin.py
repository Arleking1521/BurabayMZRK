from django.contrib import admin

from .models import Managers, Contacts

# Register your models here.

admin.site.register(Managers)
admin.site.register(Contacts)
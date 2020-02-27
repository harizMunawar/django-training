from django.contrib import admin
from . import models

class menuAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']

admin.site.register(models.menu, menuAdmin)
admin.site.register(models.Rating)
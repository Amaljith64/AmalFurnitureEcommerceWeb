from django.contrib import admin
from . models import *

# Register your models here.

class catadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}  # prepopulated is used to add slug automatically while typping name
admin.site.register(categ,catadmin)



class prodadmin(admin.ModelAdmin):
   prepopulated_fields = {'slug':('name',)}
admin.site.register(products,prodadmin)
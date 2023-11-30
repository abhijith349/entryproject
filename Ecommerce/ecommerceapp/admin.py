from django.contrib import admin
from .models import product
# Register your models here.
class productAdmin(admin.ModelAdmin):
    list_display=['id','name','brand','price','description']
    ordering =('name',)
    search_fields= ('name','brand')


admin.site.register(product,productAdmin)
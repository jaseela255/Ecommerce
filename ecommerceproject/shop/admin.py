from django.contrib import admin
from . models import category,product

# Register your models here.
class cateoryadmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}
admin.site.register(category,cateoryadmin)


class productadmin(admin.ModelAdmin):
    list_display=['name','stock','price','available','created','updated']
    list_editable=['stock','price','available']
    prepopulated_fields={'slug':('name',)}
    list_per_page=20
admin.site.register(product,productadmin)
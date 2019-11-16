from django.contrib import admin
from webapp.models import Product, Otziv

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'description')
    list_filter = ('category',)


class OtzivAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'description', 'ocenka')
    # inlines = (ProductAdmin)


admin.site.register(Product)
admin.site.register(Otziv)
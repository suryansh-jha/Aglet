from django.contrib import admin

from .models import Product, Detail, ShippingAddress, comment, ProductPayment


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'stock', 'rating')


class DetailAdmin(admin.ModelAdmin):
    list_display = ('rating', 'deliver_by', 'description')


class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('shipping_address_1', 'shipping_address_2', 'shipping_address_3')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('product', 'commenter_name', 'comment_body', 'date_added')


admin.site.register(Product, ProductAdmin)
admin.site.register(Detail, DetailAdmin)
admin.site.register(ShippingAddress, ShippingAddressAdmin)
admin.site.register(comment),
admin.site.register(ProductPayment)

from django.contrib import admin
from .models import Brand,Category,Product,Reviews,Cart,Order,Invoice, Favourites, WishList

# Register your models here.
admin.site.register(Category)
admin.site.register(Reviews)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Invoice)

class brand_modify(admin.ModelAdmin):
    fields = ['brand_name','user']
    readonly_fields=('user',)
    def get_queryset(self, request):
        if request.user.is_staff and not request.user.is_superuser:
            Brand.user = request.user
            return Brand.objects.filter(user=request.user)
        else:
            Brand.user = request.user
            return super().get_queryset(request)

admin.site.register(Brand, brand_modify)

class product_modify(admin.ModelAdmin):
    readonly_fields=('brand',)

    def get_queryset(self, request):
        if request.user.is_staff and not request.user.is_superuser:
            return Product.objects.filter(brand=request.user.brand)
        else:
            # Product.brand = request.user.brand
            return super().get_queryset(request)

    def get_form(self, request, obj=None, **kwargs):
        # here insert/fill the current user name or id from request
            Product.brand = request.user.brand
            return super().get_form(request, obj, **kwargs)

    


admin.site.register(Product, product_modify)

admin.site.register(Favourites)
admin.site.register(WishList)
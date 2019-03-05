from django.contrib import admin
from app.activity.models import Discount, SpecialOffer
# Register your models here.

@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('coupon_name','coupon_type','coupon_value','useless')


@admin.register(SpecialOffer)
class SPAdmin(admin.ModelAdmin):
    list_display = ('sp_name','sp_type')
from django.contrib import admin
from app.user.models import User, Lecturer, SpendRecord, RechargeRecord
from pure_pagination import Paginator


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_level', 'user_eng_level')
    search_fields = ['user_name']
    list_filter = ['user_name']
    list_per_page = 10
    list_max_show_all = 200
    paginator = Paginator
    filter_horizontal = ('expect_skill', 'discount_coupon')

@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ('lec_name', 'lec_idcard', 'lec_level',)
    search_fields = ['lec_name']
    list_filter = ['lec_name']
    list_per_page = 10
    list_max_show_all = 200
    paginator = Paginator
    filter_horizontal = ('lec_skill',)


@admin.register(SpendRecord)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'count', )



@admin.register(RechargeRecord)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'count', )

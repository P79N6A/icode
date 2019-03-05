from django.db import models
# from app.course.models import CurriculumSystem

class Discount(models.Model):
    """折扣券活动"""
    TYPE = (("percent","折扣百分比"),("decrease","减免数额"))
    coupon_name = models.CharField(verbose_name="折扣券名称" ,max_length=255)
    coupon_type = models.CharField(verbose_name="折扣券类型" ,max_length=255, choices=TYPE)
    coupon_value = models.FloatField(verbose_name="折扣券面额")  # 0.8  100
    create_time = models.DateTimeField(verbose_name="领取日期", auto_now_add=True)
    validity_time = models.DateTimeField(verbose_name="有效期")
    useless = models.BooleanField(verbose_name="是否失效", default=False)

    class Meta:
        verbose_name = "折扣券活动"
        verbose_name_plural = verbose_name
        db_table = "code_activity_discount"
        ordering = ['-id']

    def __str__(self):
        return self.coupon_name


class SpecialOffer(models.Model):
    """全场优惠活动"""
    TYPE = (("percent","折扣百分比"),("decrease","减免数额"), ("free","免费"))
    sp_name = models.CharField(verbose_name="活动名称" ,max_length=255)
    sp_type = models.CharField(verbose_name="活动类型" ,max_length=255, choices=TYPE)
    sp_value = models.FloatField(verbose_name="活动面额", default=0)  # 0.8  100
    create_time = models.DateTimeField(verbose_name="创建日期", auto_now_add=True)
    start_time = models.DateTimeField(verbose_name="起始时间")
    end_time = models.DateTimeField(verbose_name="结束时间")
    # useless = models.BooleanField(verbose_name="是否失效", default=False)
    # range = models.ManyToManyField(CurriculumSystem, verbose_name="课程范围", null=True, blank=True)

    class Meta:
        verbose_name = "范围活动"
        verbose_name_plural = verbose_name
        db_table = "code_activity_sp"
        ordering = ['-id']

    def __str__(self):
        return self.sp_name
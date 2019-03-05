from django.db import models
from app.other.models import Skill
from app.activity.models import Discount

class User(models.Model):
    "用户"
    LEVEL = (("primary","小学"),("middle","初中"),("high","高中"), ("university", "大学"),
             ("master", "更高学历"), ("social","社会"))

    LEVEL_ENG = (("cet4","英语四级"), ("cet6", "英语六级"), ("master","精通英语"),
                 ("normal","普通读写"), ("poor", "入门基础"))

    user_name = models.CharField(verbose_name="用户名", default="匿名",max_length=255)
    user_phone = models.CharField(verbose_name="手机号", default="", max_length=255)
    user_avatar = models.URLField(verbose_name="用户头像链接",default="")
    user_address = models.CharField(verbose_name="用户详情住址", default="", max_length=255)
    user_level = models.CharField(verbose_name="用户年级", choices=LEVEL, max_length=255)
    user_age = models.IntegerField(verbose_name="用户年龄")
    user_eng_level = models.CharField(verbose_name="用户英语能力", choices=LEVEL_ENG, max_length=255)
    expect_skill = models.ManyToManyField(Skill, verbose_name="期望技能")
    discount_coupon = models.ManyToManyField(Discount, verbose_name="拥有的优惠券", null=True, blank=True)
    # 所有点赞的课程
    # 所有阅读的历史
    user_money = models.IntegerField(verbose_name="账户余额", default=0)
    user_join_time = models.DateTimeField(auto_now_add=True, verbose_name="加入时间")


    class Meta:
        verbose_name = "注册用户"
        verbose_name_plural = verbose_name
        db_table = "code_user_user"
        ordering = ['-id']

    def __str__(self):
        return self.user_name


class Lecturer(models.Model):
    "讲师"
    LEVEL = (("primary", "小学"), ("middle", "初中"), ("high", "高中"), ("university", "大学"),
             ("graduate", "研究生"), ("master", "博士"), ("social", "社会"))

    lec_name = models.CharField(verbose_name="讲师姓名", null=False ,max_length=255)
    lec_idcard = models.CharField(verbose_name="讲师身份证号", null=False, max_length=255)
    lec_avatar = models.URLField(verbose_name="讲师头像链接",default="")
    lec_address = models.CharField(verbose_name="讲师住址", default="", max_length=255)
    lec_level = models.CharField(verbose_name="讲师学历", choices=LEVEL, max_length=255)
    lec_age = models.IntegerField(verbose_name="讲师年龄")
    lec_skill = models.ManyToManyField(Skill, verbose_name="讲师技能")

    lec_desc = models.CharField(verbose_name="讲师描述",  max_length=255)
    lec_join_time = models.DateTimeField(auto_now_add=True, verbose_name="加入时间")

    class Meta:
        verbose_name = "讲师管理"
        verbose_name_plural = verbose_name
        db_table = "code_user_lecturer"
        ordering = ['-id']

    def __str__(self):
        return self.lec_name




class RechargeRecord(models.Model):
    """充值记录"""
    user =  models.ForeignKey(User, verbose_name="充值用户" , on_delete=models.CASCADE)
    count = models.IntegerField(verbose_name="充值金额")
    code = models.CharField(verbose_name="订单号", max_length=255)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = "充值记录"
        verbose_name_plural = verbose_name
        db_table = "code_user_recharge"
        ordering = ['-id']



class SpendRecord(models.Model):
    """购买记录"""
    user = models.ForeignKey(User, verbose_name="购买用户", on_delete=models.CASCADE)
    count = models.IntegerField(verbose_name="花费金额")
    code = models.CharField(verbose_name="订单号", max_length=255)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = "购买记录"
        verbose_name_plural = verbose_name
        db_table = "code_user_spend"
        ordering = ['-id']
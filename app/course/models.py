from django.db import models
from app.user.models import Lecturer, User
from app.comment.models import Discuss
from app.activity.models import SpecialOffer

class Course(models.Model):
    """单节课程"""
    lecture = models.ForeignKey(Lecturer, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255, verbose_name="标题")
    picture = models.CharField(max_length=255, verbose_name="图标链接", default="")
    spend = models.IntegerField(verbose_name="资费")
    desc = models.CharField(max_length=255, verbose_name="描述")
    content = models.TextField(verbose_name="内容")
    count = models.IntegerField(verbose_name="访问次数")
    like =  models.IntegerField(verbose_name="点赞数")
    like_users = models.ManyToManyField(User, verbose_name="所有点赞的用户", null=True, blank=True)
    comment_users = models.ManyToManyField(Discuss, verbose_name="所有用的评论", null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = "单个课程"
        verbose_name_plural = verbose_name
        db_table = "code_course_signal"
        ordering = ['-id']

    def __str__(self):
        return self.name

class CurriculumSystem(models.Model):
    """课程大纲"""
    TYPE = (("online", "线上"), ("offline", "线下"))
    courses = models.ManyToManyField(Course, verbose_name="大纲对应的所有课时")
    course_picture = models.CharField(max_length=255, verbose_name="图标链接", default="")
    course_name = models.CharField(max_length=255, verbose_name="课程名")
    course_count = models.IntegerField(verbose_name="课时数")
    course_total_spend = models.IntegerField(verbose_name="总资费")
    course_type = models.CharField(max_length=255, verbose_name="课程类别(线下OR线上)", choices=TYPE)
    course_desc = models.CharField(max_length=255, verbose_name="大纲描述")
    course_user_join = models.ManyToManyField(User, verbose_name="所有加入的用户", null=True, blank=True)
    # 参与的活动，指定全课程可使用活动优惠
    activity = models.OneToOneField(SpecialOffer, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "课程大纲"
        verbose_name_plural = verbose_name
        db_table = "code_course_system"
        ordering = ['-id']

    def __str__(self):
        return self.course_name



from django.db import models

class Skill(models.Model):
    """技能"""
    skill_name =  models.CharField(verbose_name="技能名称" ,max_length=255)
    skill_pic = models.URLField(verbose_name="技能图标" ,max_length=255, default="")
    skill_desc = models.CharField(verbose_name="技能描述" ,max_length=255, default="")

    class Meta:
        verbose_name = "技能树"
        verbose_name_plural = verbose_name
        db_table = "code_other_skills"
        ordering = ['-id']

    def __str__(self):
        return self.skill_name


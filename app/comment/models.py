from django.db import models
from app.user.models import User

class Discuss(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(verbose_name="评论内容", max_length=255)


    class Meta:
        verbose_name = "评论"
        verbose_name_plural = verbose_name
        db_table = "code_comments"
        ordering = ['-id']

    def __str__(self):
        size = len(str(self.comment))
        if size > 20:
            return self.comment[:20] + '...'
        else:
            return self.comment
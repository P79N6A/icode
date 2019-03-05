from django.contrib import admin
from app.comment.models import Discuss
from pure_pagination import Paginator


@admin.register(Discuss)
class CommentAdmin(admin.ModelAdmin):
    list_display = ( 'user', 'comment')
    list_per_page = 10
    list_max_show_all = 200
    paginator = Paginator
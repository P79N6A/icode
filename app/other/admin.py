from django.contrib import admin
from app.other.models import Skill
from pure_pagination import Paginator

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('skill_name',)
    list_per_page = 10
    list_max_show_all = 200
    paginator = Paginator
from django.contrib import admin
from app.course.models import Course, CurriculumSystem
from pure_pagination import Paginator


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'spend')
    search_fields = ['name']
    list_filter = ['name']
    list_per_page = 10
    list_max_show_all = 200
    paginator = Paginator
    filter_horizontal = ('like_users', 'comment_users')


@admin.register(CurriculumSystem)
class CurriculumSystemAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'course_count', 'course_total_spend')
    search_fields = ['course_name']
    list_filter = ['course_name']
    list_per_page = 10
    list_max_show_all = 200
    paginator = Paginator
    filter_horizontal = ('courses','course_user_join', )





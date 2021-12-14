from django.contrib import admin
from .models import Dept, Course, Book, Teacher, C2B2T, U2G2M

# Register your models here.

# 注册Dept到admin中
admin.site.register(Dept)
admin.site.register(Course)
admin.site.register(Book)
admin.site.register(Teacher)
admin.site.register(C2B2T)
admin.site.register(U2G2M)

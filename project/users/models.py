from django.db import models
from django.contrib.auth.models import User
from company_training.models import Dept

# Create your models here.


# 用户扩展信息
class Profile(models.Model):
    # 与 User 模型构成一对一的关系
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # 姓名
    name = models.CharField(max_length=13, verbose_name="姓名", null=False, blank=False)
    # 性别
    gender = models.CharField(max_length=8, choices=(('male', '男'), ('female', '女')), verbose_name="性别", null=True,
                              blank=True)
    # 年龄
    age = models.IntegerField(verbose_name="年龄", null=True, blank=True)
    # 学历
    education = models.CharField(max_length=12, choices=(('high school', '高中'), ('bachelor', '本科'),
                                                        ('postgraduate', '研究生')),
                                 verbose_name="学历", null=True, blank=True)
    # 电话号码字段
    phone = models.CharField(max_length=20, blank=True)
    # 个人简介
    bio = models.TextField(max_length=500, blank=True)
    # 是否是经理
    is_manager = models.BooleanField(default=False, verbose_name="是否是经理")
    # 是否是讲师
    is_teacher = models.BooleanField(default=False, verbose_name="是否是讲师")
    # 所属部门
    # dept = models.CharField(max_length=10, verbose_name="所属部门", null=True, blank=True)

    dept = models.ForeignKey(Dept, on_delete=models.DO_NOTHING, verbose_name="所属部门", null=True, blank=True)

    class Meta:
        verbose_name = '详细信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return 'user {}'.format(self.user.username)

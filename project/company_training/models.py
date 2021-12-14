from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# 部门

class Dept(models.Model):
    # 部门id
    dept_id = models.IntegerField(primary_key=True, verbose_name="部门id", null=False, blank=False)
    # 部门名称
    dept_name = models.CharField(max_length=13, verbose_name="部门名称", null=False, blank=False)

    # 内部类 class Meta 用于给 model 定义元数据
    class Meta:
        # ordering 指定模型返回的数据的排列顺序
        # '-deptid' 表明数据应该以倒序排列
        ordering = ('dept_id',)
        verbose_name = '部门'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%d: %s' % (self.dept_id, self.dept_name)


# 课程
class Course(models.Model):
    # 课程id
    course_id = models.IntegerField(primary_key=True, verbose_name="课程id", null=False, blank=False)
    # 课程名称
    course_name = models.CharField(max_length=13, verbose_name="课程名称", null=False, blank=False)
    # 课程类别
    course_type = models.CharField(max_length=13, verbose_name="课程类别", null=True, blank=True)

    # 内部类 class Meta 用于给 model 定义元数据
    class Meta:
        # ordering 指定模型返回的数据的排列顺序
        # '-deptid' 表明数据应该以倒序排列
        ordering = ('course_id',)
        verbose_name = '课程'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%d: %s' % (self.course_id, self.course_name)


# 教材
class Book(models.Model):
    # 教材id
    book_id = models.IntegerField(primary_key=True, verbose_name="教材id", null=False, blank=False)
    # 教材名称
    book_name = models.CharField(max_length=13, verbose_name="教材名称", null=False, blank=False)
    # 教材价格
    book_price = models.DecimalField(verbose_name="教材价格", max_digits=8,
                                     decimal_places=2, null=True, blank=True)
    book_pubtdate = models.DateField()

    # 内部类 class Meta 用于给 model 定义元数据
    class Meta:
        # ordering 指定模型返回的数据的排列顺序
        # '-deptid' 表明数据应该以倒序排列
        ordering = ('book_id',)
        verbose_name = '教材'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%d: %s' % (self.book_id, self.book_name)


# 讲师
class Teacher(models.Model):
    # 讲师id
    teacher_id = models.IntegerField(primary_key=True, verbose_name="讲师id", null=False, blank=False)
    # 讲师名称
    teacher_name = models.CharField(max_length=13, verbose_name="讲师姓名", null=False, blank=False)
    # 讲师性别
    gender = models.CharField(max_length=8, choices=(('male', '男'), ('female', '女')), verbose_name="讲师性别", null=True,
                              blank=True)
    # 年龄
    age = models.IntegerField(verbose_name="年龄", null=True, blank=True)
    # 学历
    education = models.CharField(max_length=12, choices=(('high school', '高中'), ('bachelor', '本科'),
                                                         ('postgraduate', '研究生'), ('doctor', '博士')),
                                 verbose_name="学历", null=True, blank=True)
    # 电话号码字段
    phone = models.CharField(max_length=20, blank=True)
    # 个人简介
    bio = models.TextField(max_length=500, blank=True)
    # 是否是外聘
    is_external = models.BooleanField(default=False, verbose_name="是否是外聘")

    # 内部类 class Meta 用于给 model 定义元数据
    class Meta:
        # ordering 指定模型返回的数据的排列顺序
        # '-deptid' 表明数据应该以倒序排列
        ordering = ('teacher_id',)
        verbose_name = '讲师'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%d: %s' % (self.teacher_id, self.teacher_name)


# 课程-教材-讲师
class C2B2T(models.Model):
    # 序列id
    c2b2t_id = models.IntegerField(primary_key=True, verbose_name="序列id", null=False, blank=False)
    # 课程id
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # 讲师id
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    # 教材id
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING)
    # 开课时间
    begin_time = models.DateField()
    # 学时（h）
    period = models.IntegerField(verbose_name="学时(h)", null=False, blank=False)

    # 内部类 class Meta 用于给 model 定义元数据
    class Meta:
        # ordering 指定模型返回的数据的排列顺序
        # '-deptid' 表明数据应该以倒序排列
        ordering = ('-c2b2t_id',)
        verbose_name = '课程_教材_讲师'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%d' % self.c2b2t_id


# 员工-课程序列
class U2G2M(models.Model):
    # 员工id
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 序列id
    c2b2t = models.ForeignKey(C2B2T, on_delete=models.CASCADE)
    # 成绩
    grade = models.IntegerField(verbose_name="成绩", default=0)

    class Meta:
        unique_together = ("user", "c2b2t")
        ordering = ('-c2b2t',)
        verbose_name = '员工_课程序列'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%d %d' % (self.user.id, self.c2b2t.c2b2t_id)

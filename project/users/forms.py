# 引入表单类
from django import forms
from .models import Profile
# 引入 User 模型
from django.contrib.auth.models import User


# 登录表单，继承了 forms.Form 类
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


# 修改profile
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('gender', 'age', 'education', 'phone', 'bio')

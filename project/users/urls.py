from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    # 用户登录
    path('login/', views.user_login, name='login'),
    # 用户登出
    path('/logout/', views.user_logout, name='logout'),
    # 用户信息
    path('  edit/<int:id>/', views.profile_edit, name='edit'),

]

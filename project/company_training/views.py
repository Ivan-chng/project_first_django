from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import U2G2M, C2B2T, Course, Teacher
from django.contrib.auth.models import User
from users.models import Profile
from django.db.models import F, Q


# Create your views here.

def index(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'company_training/index.html', context={
        'title': '公司培训系统首页',
        'welcome': '欢迎访问公司培训系统首页',
        'profile': profile,
    })


# 增加学员课程 u2g2m
@csrf_exempt
# @login_required(login_url='/users/login/')
def add_u2g2m(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        c2b2t_id = request.POST.get("c2b2t")
        user_id = request.POST.get("user")
        user = User.objects.get(id=user_id)
        c2b2t = C2B2T.objects.get(c2b2t_id=c2b2t_id)
        U2G2M.objects.create(user=user, c2b2t=c2b2t, grade=0)

        return HttpResponse("success")

    c2b2t_list = C2B2T.objects.all()
    user_list = User.objects.all()
    return render(request, "company_training/add_u2g2m.html",
                  {'title': '员工选课', 'topic': '为员工增加课程',
                   "c2b2t_list": c2b2t_list,
                   "user_list": user_list,
                   'profile': profile,
                   })


@csrf_exempt
def query_u2g2m(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == "GET":
        if not profile.is_manager:
            # 员工查询
            ret_list = U2G2M.objects.filter(user=request.user).values("id",
                                                                      "c2b2t__c2b2t_id",
                                                                      "c2b2t__course__course_name",
                                                                      "user__id",
                                                                      "user__profile__name",
                                                                      "grade")
            context = {"ret_list": ret_list, 'topic': '查看我的课程成绩', 'title': '查看成绩',
                       'profile': profile}
            return render(request, "company_training/query_u2g2m.html",
                          context=context)
        else:
            # 经理查询
            # 未查询默认显示全部成绩结果

            # 获取表中的可选值
            c2b2t_list = C2B2T.objects.all()
            course_list = Course.objects.all()
            u2g2m_list = U2G2M.objects.all()
            profile_list = Profile.objects.all()

            # 显示查询结果
            ret_list = U2G2M.objects.all().values("id",
                                                  "c2b2t__c2b2t_id",
                                                  "c2b2t__course__course_name",
                                                  "user__id",
                                                  "user__profile__name",
                                                  "grade")
            context = {"ret_list": ret_list,
                       'topic': '查看员工课程成绩',
                       'title': '查看成绩',
                       "c2b2t_list": c2b2t_list,
                       "course_list": course_list,
                       "u2g2m_list": u2g2m_list,
                       "profile_list": profile_list,
                       'profile': profile,
                       }
            return render(request, "company_training/query_u2g2m.html",
                          context=context)

    else:
        if not profile.is_manager:
            return HttpResponse("只有经理才能查询所有人成绩")
        else:
            # 经理查询
            # 多条件查询
            c2b2t_id = request.POST.get("c2b2t_id")
            cname = request.POST.get("cname")
            userid = request.POST.get("userid")

            con = Q()
            q1 = Q()
            q1.connector = 'AND'  # q1对象表示‘AND’关系，也就是说q1下的条件都要满足‘AND’

            q2 = Q()
            q2.connector = 'OR'
            # 判断前台传过来的值是否存在，存在的话追加到去Q对象中，不存在的话可以赋一个空值
            if c2b2t_id:
                q1.children.append(('c2b2t__c2b2t_id', c2b2t_id))
            else:
                pass

            # cname
            if cname:
                q1.children.append(('c2b2t__course__course_name', cname))
            else:
                pass

            # userid
            if userid:
                q1.children.append(('user__id', int(userid)))
            else:
                pass

            # 把q1和q2对象添加到总的Q对象
            con.add(q1, 'AND')
            con.add(q2, 'AND')

            c2b2t_list = C2B2T.objects.all()
            course_list = Course.objects.all()
            u2g2m_list = U2G2M.objects.all()
            profile_list = Profile.objects.all()

            # 显示查询结果
            ret_list = U2G2M.objects.filter(con).values("id",
                                                        "c2b2t__c2b2t_id",
                                                        "c2b2t__course__course_name",
                                                        "user__id",
                                                        "user__profile__name",
                                                        "grade")
            context = {"ret_list": ret_list,
                       'topic': '查看员工课程成绩',
                       'title': '查看成绩',
                       "c2b2t_list": c2b2t_list,
                       "course_list": course_list,
                       "u2g2m_list": u2g2m_list,
                       "profile_list": profile_list,
                       'c2b2t_id': c2b2t_id,
                       'cname': cname,
                       'userid': userid,
                       'profile': profile,
                       }

            return render(request, "company_training/query_u2g2m.html",
                          context=context)


def query_c2b2t(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == "GET":
        if not profile.is_manager:
            # 员工查询
            ret_list = U2G2M.objects.filter(user=request.user).values("id",
                                                                      "c2b2t__c2b2t_id",  # 课程序列
                                                                      "c2b2t__course__course_name",  # 课程名称
                                                                      "user__id",  # 员工id
                                                                      "user__profile__name",  # 员工姓名
                                                                      "c2b2t__teacher__teacher_name",  # 讲师姓名
                                                                      "c2b2t__begin_time",  # 课程开始时间
                                                                      "c2b2t__period",  # 学时
                                                                      )
            context = {"ret_list": ret_list, 'topic': '查看我的课程', 'title': '查看课表',
                       'profile': profile}
            return render(request, "company_training/query_c2b2t.html",
                          context=context)
        else:
            # 经理查询
            # 未查询默认显示全部成绩结果

            # 获取表中的可选值
            c2b2t_list = C2B2T.objects.all()  # 课程序号查询
            course_list = Course.objects.all()  # 课程名称查询
            u2g2m_list = U2G2M.objects.all()  #
            profile_list = Profile.objects.all()  # 员工姓名查询
            teacher_list = Teacher.objects.all()  # 讲师姓名查询

            # 显示查询结果
            ret_list = U2G2M.objects.filter(user=request.user).values("id",
                                                                      "c2b2t__c2b2t_id",  # 课程序列
                                                                      "c2b2t__course__course_name",  # 课程名称
                                                                      "user__id",  # 员工id
                                                                      "user__profile__name",  # 员工姓名
                                                                      "c2b2t__teacher__teacher_name",  # 讲师姓名
                                                                      "c2b2t__begin_time",  # 课程开始时间
                                                                      "c2b2t__period",  # 学时
                                                                      )
            context = {"ret_list": ret_list,
                       'topic': '查看员工课程',
                       'title': '查看课程',
                       "c2b2t_list": c2b2t_list,
                       "course_list": course_list,
                       "u2g2m_list": u2g2m_list,
                       "profile_list": profile_list,
                       'profile': profile,
                       'teacher_list': teacher_list,
                       }
            return render(request, "company_training/query_c2b2t.html",
                          context=context)

    else:
        if not profile.is_manager:
            return HttpResponse("只有经理才能查询所有人课程")
        else:
            # 经理查询
            # 多条件查询
            c2b2t_id = request.POST.get("c2b2t_id")
            cname = request.POST.get("cname")
            userid = request.POST.get("userid")
            tname = request.POST.get("tname")

            con = Q()
            q1 = Q()
            q1.connector = 'AND'  # q1对象表示‘AND’关系，也就是说q1下的条件都要满足‘AND’

            q2 = Q()
            q2.connector = 'OR'
            # 判断前台传过来的值是否存在，存在的话追加到去Q对象中，不存在的话可以赋一个空值
            if c2b2t_id:
                q1.children.append(('c2b2t__c2b2t_id', c2b2t_id))
            else:
                pass

            # cname
            if cname:
                q1.children.append(('c2b2t__course__course_name', cname))
            else:
                pass

            # userid
            if userid:
                q1.children.append(('user__id', int(userid)))
            else:
                pass
            # tname
            if tname:
                q1.children.append(('c2b2t__teacher__teacher_name', tname))
            else:
                pass

            # 把q1和q2对象添加到总的Q对象
            con.add(q1, 'AND')
            con.add(q2, 'AND')

            c2b2t_list = C2B2T.objects.all()
            course_list = Course.objects.all()
            u2g2m_list = U2G2M.objects.all()
            profile_list = Profile.objects.all()
            teacher_list = Teacher.objects.all()

            # 显示查询结果

            ret_list = U2G2M.objects.filter(con).values("id",
                                                        "c2b2t__c2b2t_id",  # 课程序列
                                                        "c2b2t__course__course_name",  # 课程名称
                                                        "user__id",  # 员工id
                                                        "user__profile__name",  # 员工姓名
                                                        "c2b2t__teacher__teacher_name",  # 讲师姓名
                                                        "c2b2t__begin_time",  # 课程开始时间
                                                        "c2b2t__period",  # 学时
                                                        )
            context = {"ret_list": ret_list,
                       'topic': '查看员工课程',
                       'title': '查看课程',
                       "c2b2t_list": c2b2t_list,
                       "course_list": course_list,
                       "u2g2m_list": u2g2m_list,
                       "profile_list": profile_list,
                       'teacher_list': teacher_list,
                       'c2b2t_id': c2b2t_id,
                       'cname': cname,
                       'userid': userid,
                       'profile': profile,
                       'tname': tname
                       }

            return render(request, "company_training/query_c2b2t.html",
                          context=context)


def edit_u2g2m(request, id):
    u2g2m_list = U2G2M.objects.get(id=id)
    profile = Profile.objects.get(user=request.user)

    # 判断是否是经理
    if not profile.is_manager:
        return HttpResponse("你没有权限修改成绩")

    edit_u2g2m = U2G2M.objects.get(id=id)
    c2b2t_list = C2B2T.objects.all()
    user_list = User.objects.all()

    context = {'edit_u2g2m': edit_u2g2m, 'c2b2t_list': c2b2t_list,
               'user_list': user_list, 'topic': '修改员工成绩', 'title': '修改成绩'}
    if request.method == 'GET':
        return render(request, "company_training/edit_u2g2m.html",
                      context=context)

    else:
        grade = request.POST.get("grade")
        edit_u2g2m.grade = grade
        edit_u2g2m.save()
        context = {'edit_u2g2m': edit_u2g2m, 'c2b2t_list': c2b2t_list,
                   'user_list': user_list, 'topic': '修改员工成绩', 'title': '修改成绩'}
        return redirect("company_training:edit", id=id)


def delete_u2g2m(request, id):
    u2g2m_list = U2G2M.objects.get(id=id)
    profile = Profile.objects.get(user=request.user)

    # 判断是否是经理
    if not profile.is_manager:
        return HttpResponse("你没有权限修改他人成绩")
    U2G2M.objects.get(id=id).delete()
    return redirect("company_training:query")


def test(request):
    # profile = Profile.objects.get(user=request.user)
    # if not profile.is_manager:
    # u2g2m_list = U2G2M.objects.all()
    ret_list = U2G2M.objects.all().values("id",
                                          "c2b2t__c2b2t_id",
                                          "c2b2t__course__course_name",
                                          "user__id", "user__profile__name",
                                          "grade")

    print(ret_list)
    return HttpResponse("success")

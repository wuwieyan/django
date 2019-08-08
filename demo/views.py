from datetime import date, timedelta, datetime
from django.shortcuts import render
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect,JsonResponse
from django.template import loader,RequestContext
from demo.models import BookInfo


def my_render(request,template_path,context_dict):

    temp = loader.get_template(template_path)
    # context=RequestContext(request,context_dict)
    context=context_dict
    res_html=temp.render(context)
    return HttpResponse(res_html)


def index(request):
   from django.utils.timezone import now
   return my_render(request,'booktest/index.html',{'now':now,'list':list(range(1,9))})


def  show_books(request):
    # 显示图书信息
    # 通过M查找数据库中数据
    books=BookInfo.objects.all()
    print("********",books)
    return  my_render(request,'booktest/show_books.html',{'books':books})


def detail(request,bid):
   # num='a'+1
    # 根据bid查询图书信息
    book=BookInfo.objects.get(id=bid)
    # 查询和book相关联的任务信息
    heros=book.heroinfo_set.all()
    return  my_render(request,'booktest/detail.html',{'heros':heros,'book':book})


# 新增一本图书
def  create(request):
    # 创建一个bookinfo对象
    b=BookInfo()
    b.btitle='三国演义'
    b.bpub_date=date(1999,1,1)
    b.bread=1
    b.isDelete=False
    b.save()

    # 返回应答
   # return HttpResponse("新增成功")

     # 新增后仍返回当前页面，使用重定向

    return HttpResponseRedirect('/show_books')


def delete(request,bid):
    book=BookInfo.objects.get(id=bid)
    book.delete()
    return HttpResponseRedirect('/show_books')


def  login(request):
    return my_render(request,'booktest/login.html',{})


# 登录校验视图
def login_check(request):
    # 1.获取登录的用户名和密码
    username=request.POST.get('username')
    password=request.POST.get('password')

    # 2.登录校验
    if username=='admin'  and password=='123456':
        return HttpResponseRedirect('/index')
    else:
        return HttpResponseRedirect('/login')


# ajax
def  ajax_test(request):
    return  my_render(request,'booktest/ajax_test.html',{})


# ajax 请求处理
def  ajax_handle(request):
    return JsonResponse({'res':1})


# 显示ajax登录页面
def  ajax_login(request):
    return my_render(request,'booktest/login_ajax.html',{})


# 设置cookie
def  set_cookie(request):
    response = HttpResponse('设置cookie')
    response.set_cookie('num',1,max_age=14*24*3600)   # 两周后过期
 #   response.set_cookie('num',1,expires=datetime.now()+timedelta(days=14))
    return response

# 获取cookie
def get_cookie(request):
    num = request.COOKIES['num']
    return HttpResponse(num)


# 设置session /set_session
def  set_session(request):
    request.session['username']='zhangsan'
    request.session['age']=18
    return  HttpResponse('设置session')

# 读取session /get_session
def get_session(request):
    username=request.session['username']
    age=request.session['age']

    request.session.set_expiry(value=None)
    return HttpResponse(username+':'+ str(age))   # 存储时是整型，读取也是整型


def tem_filter(request):
    books=BookInfo.objects.all()
    return my_render(request,'booktest/show_books1.html',{'books':books})

# 模板继承
def tem_super(request):
    return my_render(request,'booktest/child.html',{})


# 静态文件
def  static_test(request):
    return my_render(request,'booktest/static_test.html',{})
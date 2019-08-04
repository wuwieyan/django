from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
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
    # 根据bid查询图书信息
    book=BookInfo.objects.get(id=bid)
    # 查询和book相关联的任务信息
    heros=book.heroinfo_set.all()
    return  my_render(request,'booktest/detail.html',{'heros':heros,'book':book})


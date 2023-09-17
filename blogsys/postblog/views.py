from django.shortcuts import render
from . import models
from django.core.paginator import Paginator

# Create your views here.
def index(request, num = 1):
    num = int(num)
    if request.method == 'GET':
        bloglist = models.Blog.objects.all().order_by('created')
        page_objs = Paginator(bloglist, 2)
        page_num = page_objs.num_pages
        page_blog =  page_objs.page(num)
        page_list =  range(1, page_num+1)
        

    return render(request, 'index.html', {'bloglist':page_blog, 'page_list':page_list, 'num':num})

def DeView(request, blogid = 1):
    blogid = int(blogid)
    if request.method == 'GET':
        blog_obj = models.Blog.objects.get(id = blogid)
    return render(request, 'detail.html', locals())
    # return render(request, 'detail.html', {'blog_obj':blog_obj})

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request, 'about.html')

# 分类显示博客列表视图函数
def getBlogByCid(request, cid):
    cid = int(cid)
    c_blog = models.Blog.objects.filter(category_id = cid)

    return render(request, 'bloglist.html',{'c_blog':c_blog})

# 分档显示博客列表视图函数
def getBlogByGuidang(request, year, month):
    year = int(year)
    month = int(month)

    c_blog = models.Blog.objects.filter(created__year = year, created__month = month)

    return render(request, 'bloglist.html', {'c_blog':c_blog})





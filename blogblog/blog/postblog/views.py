from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator

from postblog import models

# Create your views here.
def IndexView(request, num = 1):
    num = int(num)
    if request.method == 'GET':
        postlist = models.Post.objects.all().order_by('-created')
        page_obj = Paginator(postlist, 2)
        page_num = int(page_obj.num_pages)
        page_post = page_obj.page(num)
        page_list = range(1,page_num+1)
        return render(request, 'index.html', {'postlist':page_post, 'page_list':page_list,'num':num})


def DeView(request, postid = 1):
    postid = int(postid)
    if request.method == 'GET':
        post_obj = models.Post.objects.get(id = postid)
        return render(request, 'detail.html',{'post_obj':post_obj})
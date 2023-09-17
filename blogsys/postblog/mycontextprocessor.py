# coding=utf-8
from . import models
from django.db.models import Count
from django.db import connection

def getRightInfo(request):
    # 分类
    r_cate_blog = models.Blog.objects.values('category__cname', 'category_id').annotate(c = Count('*')).order_by('-c')

    # 近期文章
    r_recent_blog = models.Blog.objects.order_by('-created')[:4]

    # 归档
    cursor = connection.cursor()
    r_file_blog = cursor.execute("select created, count('*') as count from t_blog group by DATE_FORMAT(created, '%Y-%b') order by count desc")
    r_file_blog = cursor.fetchall()

    r_Taglist = models.Tags.objects.all()

    return {'r_cate_blog' : r_cate_blog, 'r_recent_blog' : r_recent_blog, 'r_file_blog' : r_file_blog, 'r_Taglist':r_Taglist}




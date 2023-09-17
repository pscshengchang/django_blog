from django.db import models

# Create your models here.
class Category(models.Model):
    cname = models.CharField(max_length=20, unique=True, verbose_name='类别名称')

    class Meta:
        db_table = 't_category'
        verbose_name = '类别'
        verbose_name_plural = '类别'
    
    def __str__(self):
        return self.cname

class Tags(models.Model):
    tname = models.CharField(max_length=20, unique=True, verbose_name='标签名')

    class Meta:
        db_table = 't_tags'
        verbose_name = '标签'
        verbose_name_plural = '标签'
    
    def __str__(self):
        return self.tname

class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='标题')
    desc = models.TextField(verbose_name='描述')
    content = models.TextField(verbose_name='内容')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name='类别')
    tags = models.ManyToManyField(Tags, verbose_name='标签')
    created = models.DateField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 't_blog'
        verbose_name = '帖子'
        verbose_name_plural = '帖子'
    
    def __str__(self):
        return self.title




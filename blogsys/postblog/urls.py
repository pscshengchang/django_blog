from django.urls import path,re_path
from . import views

urlpatterns = [
    # path('',views.index),
    path('index/', views.index),
    path('index/<int:num>/', views.index),
    path('get/<int:blogid>/', views.DeView),
    path('about/', views.about),
    path('contact/', views.contact),
    re_path(r'^category/(\d+)/$', views.getBlogByCid),
    re_path(r'^guidang/(?P<year>\d+)/(?P<month>\d+)/$', views.getBlogByGuidang),
]

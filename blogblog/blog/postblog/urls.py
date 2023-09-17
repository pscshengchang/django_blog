from . import views
from django.urls import path

urlpatterns = [
    path('', views.IndexView),
    path('page/<int:num>', views.IndexView),
    path('post/<int:postid>',views.DeView),
]

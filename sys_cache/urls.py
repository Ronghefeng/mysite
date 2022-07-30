from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

app_name = "sys_cache"

urlpatterns = [
    path("", cache_page(300)(views.index), name="index"),  # 缓存 index 路径的视图
    path("upload/", views.UploadView.as_view(), name="upload"),
]

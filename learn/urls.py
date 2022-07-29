from django.urls import path, re_path
from django.conf import settings
from . import views

app_name = "learn"

urlpatterns = [
    path("", views.home, name="home"),
    path("simple/", views.simple_upload, name="simple_upload"),
    path("form/", views.model_form_upload, name="model_form_upload"),
    path("add/", views.add_view, name="add"),
    path("pic_list/", views.Piclist.as_view(), name="pic_list"),
    path("pic_upload/", views.PicUpload.as_view(), name="pic_upload"),
    re_path(r"pic/(?P<pk>\d+)/$", views.PicDetail.as_view(), name="pic_detail"),
]

# 开发环境文件系统位置
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

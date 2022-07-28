from django.urls import path
from django.conf import settings
from . import views

app_name = "learn"

urlpatterns = [
    path("", views.home, name="home"),
    path("simple/", views.simple_upload, name="simple_upload"),
    path("form/", views.model_form_upload, name="model_form_upload"),
    path("add/", views.add_view, name="add"),
]

# 开发环境文件系统位置
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

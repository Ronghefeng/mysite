from django.urls import path

from . import views


app_name = "crawl"  # 使用 URLconf 命名空间，用于区分不同 app 下的 url


urlpatterns = [
    path("", views.index_view, name="index"),
    path("fetch_view/", views.fetch_view, name="fetch_view"),
    path("remove_view/", views.remove_view, name="remove_view"),
]

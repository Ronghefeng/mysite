from django.urls import path, re_path
from django.urls import register_converter


from . import views, converters

register_converter(converters.FourDigitYearConverter, "yyyy")  # 注册t自定义路径转换器

app_name = "polls"  # 使用 URLconf 命名空间，用于区分不同 app 下的 url

urlpatterns = [
    path("", views.index, name="index"),
    # path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    re_path(r"^(?P<pk>\d+)/$", views.DetailView.as_view(), name="detail"),  # 同上
    path("<int:pk>/results", views.ResultView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("year/<yyyy:year>/", views.test_converter, name="yyyy"),
    re_path(
        r"^(?:multple_params-(?P<year>\d+)/)?$", views.test_converter, name="test1"
    ),  # match ulr like  multple_params-3
    path(
        "year/<yyyy:year>/", views.test_converter, {"user_id": 111}, name="yyyy"
    ),  # 携带额外参数 user_id --- failed, can not find user_id in views
]

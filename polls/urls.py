from django.urls import path
from . import views

app_name = "polls"  # 使用 URLconf 命名空间，用于区分不同 app 下的 url

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results", views.ResultView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from login.models import OnlineUser

from .forms import LoginForm


def register(request):

    if request.method.lower() == "post":

        form = LoginForm(request.POST)

        if form.is_valid():
            form.save()
            return render(
                request, "login/login.html", {"form": form, "msg": "注册成功，请登录！"}
            )

    else:

        form = LoginForm()
    return render(request, "login/register.html", {"form": form})


def login(request):

    if request.method.lower() == "post":

        form = LoginForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            if OnlineUser.objects.filter(
                username__exact=username, password=password
            ).exists():

                response = HttpResponseRedirect("/login/detail/")

                # 使用 cookie 保存信息
                response.set_cookie("username", username, 3600)

                # 使用 session 保存信息
                request.session["username"] = username
                # 设置 session 过期时间
                request.session.set_expiry(3600)

                return response

            else:
                return HttpResponseRedirect(reverse("login:register"))

    else:
        form = LoginForm()

    return render(
        request,
        "login/login.html",
        {
            "form": form,
        },
    )


def index(request):

    username = request.COOKIES.get("username", "游客")
    # username = request.session["username"]

    return render(request, "login/index.html", {"username": username})


def logout(request):

    response = HttpResponse("logout!!")

    response.delete_cookie("username")
    # del request.session["username"]

    return response
